from django.forms import ModelForm
from .models import Vehicle, Passenger


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'admin']


class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'phone_no', 'vehicle']
