from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car # Especifica o modelo ao qual o formulario estará vinculado.
        fields = '__all__' # Define os campos do modelo que deve ser incluido no formulario

    # Criando validações para o formulario de cadastro de veiculos
    def clean_yaer(self):
        # Pegar os valores do campo "YAER" que está sendo enviado no formulario
        # cleaned_data (os dados limpos)
        yaer = self.cleaned_data.get('yaer')

        if yaer < 1975:
            # Adicionando erro ao campo yaer
            self.add_error('yaer', 'O ano de fabricação do veiculo não pode ser antes do ano 1975')
        return yaer



