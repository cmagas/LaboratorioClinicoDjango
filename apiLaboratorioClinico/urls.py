from django.urls import path
from .views import *

urlpatterns = [
    path('analisis/', analisisView.as_view()),
    path('analisis/<int:id>', analisisView.as_view())
]