from django.contrib import admin
from .models import Passenger, Vehicle

admin.site.register(Passenger)
# admin.site.register(Vehicle)


class PassengerInline(admin.TabularInline):
    model = Passenger
    # raw_id_fields = ('vehicle',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    inlines = [
        PassengerInline,
    ]
