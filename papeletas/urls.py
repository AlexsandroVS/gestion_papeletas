from django.urls import path
from .views import (
    listar_conductores,
    crear_conductor,
    editar_conductor,
    eliminar_conductor,
    listar_infracciones,
    crear_infraccion,
    editar_infraccion,
    eliminar_infraccion,
    listar_papeletas,
    crear_papeleta,
    editar_papeleta,
    eliminar_papeleta,
    inicio
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('conductores/', listar_conductores, name='listar_conductores'),
    path('conductores/crear/', crear_conductor, name='crear_conductor'),
    path('conductores/editar/<int:id>/', editar_conductor, name='editar_conductor'),
    path('conductores/eliminar/<int:id>/', eliminar_conductor, name='eliminar_conductor'),

    path('infracciones/', listar_infracciones, name='listar_infracciones'),
    path('infracciones/crear/', crear_infraccion, name='crear_infraccion'),
    path('infracciones/editar/<int:id>/', editar_infraccion, name='editar_infraccion'),
    path('infracciones/eliminar/<int:id>/', eliminar_infraccion, name='eliminar_infraccion'),

    path('papeletas/', listar_papeletas, name='listar_papeletas'),
    path('papeletas/crear/', crear_papeleta, name='crear_papeleta'),
    path('papeletas/editar/<int:id>/', editar_papeleta, name='editar_papeleta'),
    path('papeletas/eliminar/<int:id>/', eliminar_papeleta, name='eliminar_papeleta'),
]
