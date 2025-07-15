from django import forms
from cars.models import Brand, Car

# Formulario para registro de carros
class CarRegistrationForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # Campo é uma chave estrangeira da tabela Brand (Mostar todas as marcas disponiveis)
    value = forms.FloatField()
    year = forms.IntegerField()
    photo = forms.ImageField()

    # metodo para salvar o novo carro no banco de dados 
    def save(self):

        # nova instancia de carro que será salva no banco
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            value = self.cleaned_data['value'],
            year = self.cleaned_data['year'],
            photo = self.cleaned_data['photo'],
        )

        # Salva no banco de dados
        car.save()
        return car


    