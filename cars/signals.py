from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory



def car_inventory_update():
    #Somar a quantidade de registro de carros no bando de dados
    cars_count = Car.objects.all().count()
    
    #calcula a soma total da coluna value da tabela Car
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']

    # Criar um registro na tabela
    CarInventory.objects.create(
        car_count = cars_count,
        car_value = cars_value
    )


@receiver(post_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    car_inventory_update()
    

@receiver(post_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
