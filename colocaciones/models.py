from django.db import models
from django.utils import timezone

class Agencia(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
            return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    fechaDeNacimiento = models.DateField()
    tipoDeTrabajoQuePuedeRealizar = models.ForeignKey('Rubro', null=True, blank=True, on_delete=models.CASCADE)
    desocupado = models.BooleanField()
    def __str__(self):
            return self.nombre

class Empleo(models.Model):
    persona = models.ForeignKey('Persona', null=True, blank=True, on_delete=models.CASCADE)
    oferta = models.ForeignKey('Oferta', null=True, blank=True, on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', null=True, blank=True, on_delete=models.CASCADE)
    inicioContrato = models.DateField()
    finContrato = models.DateField()
    def __str__(self):
            return self.oferta

class Rubro(models.Model):
    tipoDeTrabajo = models.CharField(max_length=20)
    def __str__(self):
            return self.tipoDeTrabajo

class Oferta(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    empresa = models.ForeignKey('Empresa', null=True, blank=True, on_delete=models.CASCADE)
    necesidad = models.ForeignKey('Rubro', null=True, blank=True, on_delete=models.CASCADE)
    activa = models.BooleanField()
    inicioContrato = models.DateField()
    finContrato = models.DateField()
    def __str__(self):
            return self.id

class Empresa(models.Model):
    cuit = models.CharField(max_length=20)
    razonSocial = models.CharField(max_length=30)
    rubro = models.ForeignKey('Rubro', null=True, blank=True, on_delete=models.CASCADE)
    activa = models.BooleanField()
    def __str__(self):
            return self.razonSocial

