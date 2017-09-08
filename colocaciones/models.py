from django.db import models
from django.utils import timezone
# Create your models here.

class Agencia(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
            return self.title



class Persona(models.Model):
    dni = models.CharField(max_length=8)
    tipoDeTrabajoQuePuedeRealizar
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechaDeNcaimiento
    desocupado

class Empleo(models.Model):
    persona
    oferta
    empresa
    inicioDeContrato
    finDeContrato

class Rubro(models.Model):
    tipoDeTrabajo

class Oferta(models.Model):
    empresa
    necesidad
    fecha
    activa
    inicioContrato
    finContrato

class Empresa(models.Model):
    cuit
    razonSocial
    rubro
    listaDeOfertas
    activa

