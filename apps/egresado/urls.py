from django.conf.urls import url, include
from apps.egresado.views import EgresadoCrear, EgresadoList
from django.contrib.auth.decorators import login_required

urlpatterns=[
	url(r'^nuevo$',EgresadoCrear.as_view(),name='egresado_crear'),
	url(r'^listar$',EgresadoList.as_view(),name='egresado_listar'),
]