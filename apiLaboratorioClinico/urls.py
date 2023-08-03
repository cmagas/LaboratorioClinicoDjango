from django.urls import path
from .views import *

urlpatterns = [
    path('analisis/', analisisView.as_view()),
    path('analisis/<int:id>', analisisView.as_view()),
    path('especialidades/', especialidadView.as_view()),
    path('especialidades/<int:id>', especialidadView.as_view()),
    path('examenes/', examenView.as_view()),
    path('examenes/<int:id>', examenView.as_view()),
    path('pacientes/', pacienteView.as_view()),
    path('pacientes/<int:id>', pacienteView.as_view()),
    path('usuarios/', usuarioView.as_view()),
    path('usuarios/<int:id>', usuarioView.as_view()),
    path('medicos/', medicoView.as_view()),
    path('medicos/<int:id>', medicoView.as_view())
]