from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car # Especifica o modelo ao qual o formulario estará vinculado.
        fields = '__all__' # Define os campos do modelo que deve ser incluido no formulario




    