from django.shortcuts import render
from cars.models import Car



def car_views(request):
    car = Car.objects.all().order_by('model') ##busca todos os carros

    ## Busar carros por busca
    search = request.GET.get('search')
    if search: 
        car = car.filter(model__icontains=search)

    return render(
        request,
        'home_page.html',
        {'cars': car}   
    )

