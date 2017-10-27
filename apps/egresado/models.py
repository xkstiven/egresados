from django.db import models
from django.contrib.auth.models import User
from apps.smart_selects.db_fields import GroupedForeignKey

# Create your models here.

class Interes(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Sexo(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Pais(models.Model):
	nombre = models.CharField(max_length= 50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Departamento(models.Model):
	nombre = models.CharField(max_length= 50)
	pais = models.ForeignKey(Pais,null=False,blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

class Carrera(models.Model):
	nombre = models.CharField(max_length= 50)

	def __str__(self):
		return '{}'.format(self.nombre)

class Egresado(models.Model):
	nombre= models.CharField(max_length=50)
	apellidos = models.CharField(max_length= 100)
	codigo = models.CharField(max_length=10)
	fecha_nacimiento = models.DateField()
	carrera = models.OneToOneField(Carrera,blank=True)
	grado= models.IntegerField()
	sexo= models.OneToOneField(Sexo,blank=True)
	departamento= GroupedForeignKey(Pais,"pais")
	pais= models.ForeignKey(Pais,null=True,blank=True)
	interes = models.ManyToManyField(Interes, blank=True)