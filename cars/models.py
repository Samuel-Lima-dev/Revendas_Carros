from django.db import models


## Tabela de Marcas de carros
class Brand(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=100)

    #Retornar o nome da marca
    def __str__(self):
        return self.name


## Tabela de Carros
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True) #Chave estrangeira
    value = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # pasta onde será feito o upload da imagem

    # retornar o modelo do carro ao invés de " object " que é o padrão
    def __str__(self):
        return self.model

    
    