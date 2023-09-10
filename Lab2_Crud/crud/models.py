from django.db import models
from django.utils import timezone

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    type_document = models.CharField(max_length=20)
    document = models.PositiveSmallIntegerField()
    birthday = models.DateField() #Formato (DD-MM-AAA), {en caso de no funcionar = models.DateField(input_formats=["%d-%m-%Y"])}
    phone_number = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True) #El estado se deja como activo predeterminadamente
    register_date = models.DateTimeField(default=timezone.now) #Establece la fecha actual como predeterminada
    adress = models.CharField(max_length=30)

class Roles(models.Model):
    rol_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    create_date = models.DateTimeField(default=timezone.now) #Establece la fecha actual como predeterminada
    rol_status  = models.BooleanField(default=True) #El estado se deja como activo predeterminadamente
