from django.http import JsonResponse
from django.shortcuts import render
from .models import analisis, especialidad, examen, rol, paciente, usuario, medico, realizar_examen
from django.views.generic import View
# Create your views here.

class analisisView(View):
    def get(self, request):
        getanalisis=list(analisis.objects.values("analisis_id","analisis_nombre","analisis_fregistro","analisis_estado"))
        if len(getanalisis)>0:
            datos={'message':"success",'analisis':getanalisis}
        else:
            datos={'message':"analisis no encontrados"}
        return JsonResponse(datos)
    def post(self, request):
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass