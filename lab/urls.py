from django.urls import path
from . import views
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path(_('agregar/'), views.agregar, name='agregar'),
    path(_('consultar/'), views.consultar, name='consultar'),
    path(_('eliminar/<int:pk>'), views.eliminar, name='eliminar'),
    path(_('editar/<int:pk>'), views.editar, name='editar'),
]