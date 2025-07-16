from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Criando formulário de cadastro de usuário
def user_registration(request):

    if request.method == 'POST':
        # Pegando os dados do formulario passado pelo usuario
        user_form = UserCreationForm(request.POST)

        # Validando os dados do usuário e salvando no banco de dados
        if user_form.is_valid():
            user_form.save()

            return redirect('login')
    else:
        # Formulário de registro de usuario
        user_form = UserCreationForm()
    

    return render(
        request,
        'register_user.html',
        {'user_form': user_form}
    )



def login_view(request):

    if request.method == 'POST':
        # Capturar o usuário e senha enviado no formulário do login
        username = request.POST['username']
        password = request.POST['password']

        # Faz a verificação dos dados do usuario
        user = authenticate(username=username, password = password)

        if user is not None:
            login(request, user)
            return redirect('car_list')
        
        else:
            login_form = AuthenticationForm()
    else: 
        # Formulario de login
        login_form = AuthenticationForm()


    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )


def logout_view(request):
    logout(request)
    return redirect('car_list')