from django import forms

from apps.egresado.models import Egresado

class EgresadoForm(forms.ModelForm):
	class Meta:
		model = Egresado

		fields = [
			'nombre',
			'apellidos',
			'codigo',
			'fecha_nacimiento',
			'sexo',
			'interes',
		]

		labels = {
			'nombre':'Nombre',
			'apellidos': 'Apellidos',
			'codigo': 'Cedula',
			'fecha_nacimiento':'Fecha Nacimiento',
			'sexo':'Sexo',
			'interes':'interes',
		}

		widgets={
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'apellidos':forms.TextInput(attrs={'class':'form-control'}),
		'codigo': forms.TextInput(attrs={'class':'form-control'}),
		'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control'}),
		'sexo':forms.Select(attrs={'class':'form-control'}),
		'interes':forms.CheckboxSelectMultiple(),
		}