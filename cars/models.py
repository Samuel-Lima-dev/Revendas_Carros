from django.db import models


## Marcas 
class Brand(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


## Carros
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True)
    value = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.model

    
    