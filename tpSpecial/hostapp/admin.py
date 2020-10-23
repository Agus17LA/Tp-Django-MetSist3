from django.contrib import admin

from hostapp.models import Property, Service, Reservation


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")
    search_fields = ("title", "category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")
    list_filter = ("category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", )


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("property", "user", "final_price")


admin.site.register(Property, PropertyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Reservation, ReservationAdmin)
