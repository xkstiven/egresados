from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.egresado.forms import EgresadoForm
from apps.egresado.models import Egresado
# Create your views here.

class EgresadoCrear(CreateView):
	model = Egresado
	form_class = EgresadoForm
	template_name = 'egresado/egresado_form.html'
	success_url = reverse_lazy('egresado:egresado_listar')

class EgresadoList(ListView):
	model = Egresado
	template_name= 'egresado/egresado_list.html'

class EgresadoUpdate(UpdateView):
	model = Egresado
	form_class= EgresadoForm
	template_name= 'egresado/egresado_form.html'
	success_url = reverse_lazy('egresado:egresado_listar')

class EgresadoEliminar(DeleteView):
	model = Egresado
	template_name= 'egresado/egresado_delete.html'
	success_url= reverse_lazy('egresado:egresado_listar')
