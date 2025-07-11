from django.shortcuts import render
from cars.models import Car



def car_views(request):
    car = Car.objects.all() ##busca todos os carros

    ## Busar carros por busca
    search = request.GET.get('search')
    if search: 
        car = car.objects.filter(model__contains=search)

    return render(
        request,
        'home_page.html',
        {'cars': car}   
    )


