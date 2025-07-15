from django.shortcuts import render, redirect
from cars.models import Car
from cars.form import CarRegistrationForm


# Consulta os carros do banco e retrona para pagina html
# Consulta de forma filtrada através da buscaa do ususario
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


# 
def car_registration(request):

    if request.method == 'POST':
        #pegando os dados enviado no formulario, através do método post 
        # (request.files ) para quando o formulario estivar o atributo
        # encytype="multipart/form-data"
        new_car_form = CarRegistrationForm(request.POST, request.FILES)

        #Verificar se os dados enviado no formulario são validos
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('newcar') # redirecionar para a pagina newcar após os dados serem salvos
    else:
        new_car_form = CarRegistrationForm()
    

    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )

