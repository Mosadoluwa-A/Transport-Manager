"""ctmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ctmapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name="login_user"),
    path('home/', views.home, name="home"),
    path('logout', views.logout_user, name="logout_user"),
    path('passenger/add', views.add_passenger, name="add_passenger"),
    path('vehicle/add', views.add_vehicle, name="add_vehicle"),
    path('vehicle/<int:vehicle_id>', views.vehicle_detail, name="vehicle_detail"),
]
