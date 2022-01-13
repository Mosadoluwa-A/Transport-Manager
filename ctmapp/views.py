import os
import dotenv
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, Passenger
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from twilio.rest import Client
from .forms import PassengerForm, VehicleForm


@login_required
def home(request):
    if request.method == "GET":
        vehicles = Vehicle.objects.all()
        context = {'vehicles': vehicles, 'user': request.user}
        return render(request, 'index.html', context)
    else:
        dotenv_file = os.path.join(settings.BASE_DIR, '.env')
        if os.path.isfile(dotenv_file):
            dotenv.load_dotenv(dotenv_file)
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        # msg = request.POST['all-msg']
        # print(msg)
        passengers = Passenger.objects.filter(is_active=True)
        for passenger in passengers:
            message = client.messages \
                .create(
                    body="Hello there! welcome aboard!",
                    from_='+19377779998',
                    to="+234"+str(passenger.phone_no)
            )

        messages.success(request, "Messages Sent Successfully")
        return redirect(home)


@login_required
def vehicle_detail(request, vehicle_id):
    if request.method == "GET":
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        context = {"vehicle": vehicle}
        return render(request, 'vehicle-detail.html', context)
    else:
        vehicle = get_object_or_404(Vehicle, id=vehicle_id)
        dotenv_file = os.path.join(settings.BASE_DIR, '.env')
        if os.path.isfile(dotenv_file):
            dotenv.load_dotenv(dotenv_file)
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        msg = request.POST['all-msg']
        passengers = Passenger.objects.filter(is_active=True)
        for passenger in vehicle.passengers:
            message = client.messages \
                .create(
                    body=msg,
                    from_='+19377779998',
                    to=passenger.phone_no
            )

        messages.success(request, "Messages Sent Successfully")
        return redirect(vehicle_detail)


@login_required
def add_passenger(request):
    if request.method == "GET":
        vehicles = Vehicle.objects.all()
        context = {"vehicles": vehicles}
        return render(request, 'new-passenger.html', context)
    else:
        try:
            form = PassengerForm(request.POST)

            if form.is_valid:
                form.save()
                messages.success(request, "Passenger Added Successfully")
                return redirect(home)
            else:
                print(form.errors)
                messages.error(request, "Please fill all the fields")
                return redirect(add_passenger)
        except Exception as e:
            print(e)
            vehicles = Vehicle.objects.all()
            context = {"vehicles": vehicles}
            return render(request, 'new-passenger.html', context)


@login_required
def add_vehicle(request):
    if request.method == "GET":
        users = User.objects.all()
        context = {"users": users}
        return render(request, 'new-vehicle.html', context)
    else:
        try:
            form = VehicleForm(request.POST)
            print(request.POST['name'])
            print(request.POST['admin'])
            if form.is_valid:
                print(form.errors)
                form.save()
                messages.success(request, "Vehicle Added Successfully")
                return redirect(home)
            else:
                print(form.errors)
                messages.error(request, "Please fill all the fields")
                return redirect(add_vehicle)
        except Exception as e:
            print(e)
            users = User.objects.all()
            context = {"users": users}
            return render(request, 'new-vehicle.html', context)


def login_user(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect(home)
    elif request.method == "GET":
        return render(request, 'login.html')

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, "Sorry username and passwords did not match")
            return render(request, 'login.html')
        else:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect(home)


def logout_user(request):
    if request.method == "POST":
        logout(request)
    return redirect(login_user)
