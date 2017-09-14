from django.db import models
from django.utils import timezone

class Agencia(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
            return self.title

class Persona(models.Model):
    dni = models.CharField(max_length=8)
    tipoDeTrabajoQuePuedeRealizar = models.ForeignKey('Rubro')
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechaDeNacimiento = models.DateField()
    desocupado = models.BooleanField()
    def __str__(self):
            return self.title

class Empleo(models.Model):
    persona = models.ForeignKey('Persona')
    oferta = models.ForeignKey('Oferta')
    empresa = models.ForeignKey('Empresa')
    inicioContrato = models.DateField()
    finContrato = models.DateField()
    def __str__(self):
            return self.title

class Rubro(models.Model):
    tipoDeTrabajo = models.CharField(max_length=20)
    def __str__(self):
            return self.title

class Oferta(models.Model):
    empresa = models.ForeignKey('Empresa')
    necesidad = models.ForeignKey('Rubro')
    activa = models.BooleanField()
    inicioContrato = models.DateField()
    finContrato = models.DateField()
    def __str__(self):
            return self.title

class Empresa(models.Model):
    cuit = models.CharField(max_length=20)
    razonSocial = models.CharField(max_length=30)
    rubro = models.ForeignKey('Rubro')
    activa = models.BooleanField()
    def __str__(self):
            return self.title

