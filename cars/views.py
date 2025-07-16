from django.shortcuts import render, redirect
from cars.models import Car
from cars.form import CarModelForm

from django.views import View



# Consulta os carros do banco e retorna para pagina html
# Consulta de forma filtrada através da buscaa do ususario
class CarView(View):
    
    def get(self, request):
        cars = Car.objects.all().order_by('model')##busca todos os carros

        ## pega dados da busca do usuario
        search = request.GET.get('search')  
        if search:
            cars = cars.filter(model_icontains=search)

        return render(
            request,
            'home_page.html',
            {'cars': cars}
        )
    

class CarRegistrationView(View):

    def get(self, request):
        # Formulario de cadastro de veiculo
        new_car_form = CarModelForm()

        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )
    

    def post(self, request):
        #pegando os dados enviado no formulario, através do método post 
        # (request.files ) para quando o formulario estivar o atributo:
        # encytype="multipart/form-data"
        new_car_form = CarModelForm(request.POST, request.FILES)

        #Verificar se os dados enviado no formulario são validos
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('newcar') # redirecionar para a pagina newcar após os dados serem salvos
        
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )



