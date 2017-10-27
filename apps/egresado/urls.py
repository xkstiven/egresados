from django.conf.urls import url, include
from apps.egresado.views import EgresadoCrear, EgresadoList, EgresadoUpdate, EgresadoEliminar
from django.contrib.auth.decorators import login_required

urlpatterns=[
	url(r'^nuevo$',login_required(EgresadoCrear.as_view()),name='egresado_crear'),
	url(r'^listar$',login_required(EgresadoList.as_view()),name='egresado_listar'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(EgresadoUpdate.as_view()), name='egresado_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(EgresadoEliminar.as_view()), name='egresado_eliminar'),
]