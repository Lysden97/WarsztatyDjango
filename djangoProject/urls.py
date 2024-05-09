"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from Warsztaty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('room/new/', views.DodajSaleView.as_view(), name='dodaj_sale'),
    path('room/', views.WyswietlSaleView.as_view(), name='dostepne_sale'),
    path('room/delete/<int:pk>', views.UsunSaleView.as_view(), name='usun_sale'),
    path('room/modify/<int:pk>', views.ModyfikacjaSaliView.as_view(), name='modyfikacja_sali')
]
