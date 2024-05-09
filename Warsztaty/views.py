from django.shortcuts import render, redirect
from django.views import View
from pyexpat.errors import messages

from Warsztaty.models import Sale


# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')

class DodajSaleView(View):

    def get(self, request):
        return render(request, 'dodaj_sale.html')

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        availability = request.POST.get('availability') == 'on'

        if not name:
            return render(request, 'dodaj_sale.html',
                          {'error_name': 'Nazwa sali nie może być pusta.'})

        try:
            capacity = int(capacity)
            if capacity <=0:
                raise ValueError
        except ValueError:
            return render(request, 'dodaj_sale.html',
                          {'error_value': 'Pojemność musi być liczbą dodatnią.'})

        if Sale.objects.filter(name=name).exists():
            return render(request, 'dodaj_sale.html',
                          {'error_samename': 'Sala o podanej nazwie już istnieje'})

        Sale.objects.create(name=name, capacity=capacity, availability= availability)

        return redirect('lista_sal.html')





