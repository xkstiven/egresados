from django.db import models

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
	nombre = models.CharField(self.nombre)

	def __str__(self):
		return '{}'.format(self.nombre)

class Departamento(models.Model):
	nombre = models.CharField(self.nombre)
	pais = models.OneToOneField(Pais,blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)

class Egresado(models.Model):
	nombre= models.CharField(max_length=50)
	apellidos = models.CharField(max_length= 100)
	codigo = models.CharField(max_length=10)
	fecha_nacimiento = models.DateField()
	sexo= models.OneToOneField(Sexo,blank=True)
	interes = models.ManyToManyField(Interes, blank=True)