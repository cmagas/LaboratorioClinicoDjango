from django.urls import path
from .views import *

urlpatterns = [
    path('analisiss/', analisisView.as_view())
]