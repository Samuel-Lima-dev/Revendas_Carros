from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from cars.models import Car
from cars.form import CarModelForm


#Listar carros 
# Consulta os carros do banco e retorna para pagina html
# Consulta de forma filtrada através da buscaa do ususario
class CarView(View): 
    
    def get(self, request):
        ##busca todos os carros
        cars = Car.objects.all().order_by('model')

        ## pega dados da busca do usuario
        search = request.GET.get('search')  
        if search:
            cars = cars.filter(model__icontains=search)

        return render(
            request,
            'home_page.html',
            {'cars': cars}
        )
    

# Visualizar detalhes do carro
class CarDetailView(View):

    def get(self, request, pk):
        car_detail = Car.objects.get(pk=pk)

        return render(
            request,
            'car_details.html',
            {'car_detail': car_detail}

        )


#Proteção da view com login_required
@method_decorator(login_required(login_url='login'), name='dispatch')

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
            # redirecionar para a pagina newcar após os dados serem salvos
            return redirect('newcar') 
        
        return render(
            request,
            'new_car.html',
            {'new_car_form': new_car_form}
        )


@method_decorator(login_required(login_url='login'), name='dispatch')

class CarUpdateView(View):
    
    def get(self, request, pk):
        # buscar no banco o carro referente a pk 
        car = Car.objects.get(pk=pk)

        # Preenche o formulario com os dados recuperados do banco de dados
        # para ser renderizados no HTML
        form = CarModelForm(instance=car)
        return render(
            request, 
            'car_update.html',
            {'form': form, 'car':car}
        )
        
    def post(self, request, pk):
        car = Car.objects.get(pk=pk)

        # Pega os dados passado no formulário e atualiza o objeto car já existente
        form = CarModelForm(request.POST, instance=car)

        if form.is_valid():
            form.save()

            # Após salvar as alterações, é redirecionado para paginas de detalhes
            # passando o pk do carro que estava sendo editado
            # pois o metodo detalhes também espera a pk como parâmetro
            return redirect(
                'car_detail',
                pk=car.pk
            )
        else:
            return render(
                request, 
                'car_update.html',
                {'form': form}
            )
        

@method_decorator(login_required(login_url='login'), name='dispatch')

class CarDeleteView(View):

    def get(self, request, pk):
        car = Car.objects.get(pk=pk)

        return render(
            request,
               'car_deletion.html',
            {'car': car}
        )
    
    def post(self, request, pk):
        car = Car.objects.get(pk=pk)

        # Deleta o carro do banco de dados
        car.delete()
        
        return redirect('car_list')
        


