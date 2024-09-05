from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from main.models import Car, Client, Sale


def cars_list_view(request):
    # получите список авто
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, context={'cars': cars})  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    car = get_object_or_404(Car, id=car_id)
    template_name = 'main/details.html'
    return render(request, template_name, context={'car': car})  # передайте необходимый контекст


def sales_by_car(request, car_id):
    sales = Sale.objects.filter(car_id=car_id)
    try:
        # получите авто и его продажи
        template_name = 'main/sales.html'
        return render(request, template_name, context={'sales': sales})  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
