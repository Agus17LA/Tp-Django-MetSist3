from django.contrib import admin

from hostapp.models import Property, Reservation, ReservationDate


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day","services")
    search_fields = ("title", "category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")
    list_filter = ("category", "max_persons", "bedrooms", "bathrooms", "beds", "price_per_day")


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("property", "user", "final_price")


class ReservationDateAdmin(admin.ModelAdmin):
    list_display = ("property", "reservation", "date")


admin.site.register(Property, PropertyAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationDate, ReservationDateAdmin)