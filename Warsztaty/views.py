from django.shortcuts import render, redirect
from django.views import View
from pyexpat.errors import messages

from Warsztaty.models import Sale, Rezerwacja

import datetime

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
        projector_availability = request.POST.get('projector_availability') == 'on'

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

        Sale.objects.create(name=name, capacity=capacity, projector_availability= projector_availability)

        return redirect('dostepne_sale')


class WyswietlSaleView(View):
    def get(self, request):
       sale = Sale.objects.all()
       return render(request, 'lista_sal.html', {'sale': sale})

class UsunSaleView(View):
    def get(self, request, pk):
        try:
            sala = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return redirect('dostepne_sale')

        sala.delete()

        return redirect('dostepne_sale')

class ModyfikacjaSaliView(View):
    def get(self, request, pk):
        mod_sale = Sale.objects.get(pk=pk)
        return render(request, 'modyfikuj_sale.html', {'mod_sale': mod_sale})

    def post(self, request, pk):
       mod_sale = Sale.objects.get(pk=pk)
       name = request.POST.get('name')
       capacity = request.POST.get('capacity')
       projector_availability = request.POST.get('projector_availability') == 'on'

       if not name:
           return render(request, 'modyfikuj_sale.html', {'mod_sale': mod_sale,
                                                          'error_name': 'Nazwa sali nie może być pusta.'})

       try:
           capacity = int(capacity)
           if capacity <=0:
               raise ValueError
       except ValueError:
           return render(request, 'modyfikuj_sale.html', {'mod_sale': mod_sale,
                                                          'error_value': 'Pojemność musi być liczbą dodatnią.'})


       if name != mod_sale.name and Sale.objects.filter(name=name).first():
           return render(request, 'modyfikuj_sale.html', {'mod_sale': mod_sale,
                                                          'error_samename': 'Sala o podanej nazwie już istnieje'})


       mod_sale.name = name
       mod_sale.capacity = capacity
       mod_sale.projector_availability = projector_availability
       mod_sale.save()
       return redirect('dostepne_sale')

class RezerwacjaView(View):
    def get(self, request, sale_id):
        rezerwacja = Sale.objects.get(id=sale_id)
        return render(request, 'rezerwacja.html', {'rezerwacja': rezerwacja})

    def post(self, request, sale_id):
        sale = Sale.objects.get(id=sale_id)
        date = request.POST.get('reservation-date')
        comment = request.POST.get('comment')

        if Rezerwacja.objects.filter(sale_id=sale, date=date):
            return render(request, 'rezerwacja.html', {'sale': sale,
                                                       "error": "Sala jest już zarezerwowana!"})

        if date < str(datetime.date.today()):
            return render(request, "rezerwacja.html", {"sale": sale,
                                                       "error": "Data jest z przeszłości!"})

        Rezerwacja.objects.create(sale_id=sale, date=date, comment=comment)
        return redirect('dostepne_sale')