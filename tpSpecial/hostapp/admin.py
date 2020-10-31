from django.contrib import admin
from hostapp.models import Property, Reservation, ReservationDate, City

# Register your models here.
# https://www.hektorprofe.net/tutorial/utilizar-inlines-admin-nuestras-vistas


class ReservationDateInline(admin.TabularInline):
    model = ReservationDate
    fk_name = 'property'
    min_num = 0
    max_num = 100


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day","services")
    search_fields = ("title", "category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")
    list_filter = ("category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")
    inlines = (ReservationDateInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("property", "userFirstName", "final_price")





class ReservationDateAdmin(admin.ModelAdmin):
    list_display = ("property", "reservation", "date")
    #exclude = ("Reservation",)
    list_filter = ("date", "property")
    date_hierarchy = "date"


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", )


admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationDate, ReservationDateAdmin)
admin.site.register(City, CityAdmin)


#Links que hacen referencia a la restricción de acciones por usuarion en el admin 
#dependiendo los groups
#https://stackoverflow.com/questions/54558653/restrict-groups-in-django-admin-for-staff-user
#https://stackoverflow.com/questions/6310983/django-admin-specific-user-admin-content
