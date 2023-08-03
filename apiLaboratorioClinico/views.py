from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import render
from .models import analisis, especialidad, examen, rol, paciente, usuario, medico, realizar_examen
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class analisisView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request,id=0):
        if (id>0):
            getanalisis=list(analisis.objects.filter(analisis_id=id).values())
            if len(getanalisis)>0:
                unanalisis=getanalisis[0];
                datos={'message':"success",'analisis':getanalisis}
            else:
                datos={'message':"analisis no encontrados"}
            return JsonResponse(datos)
        else: 
            getanalisis=list(analisis.objects.values("analisis_id","analisis_nombre","analisis_fregistro","analisis_estado"))
            if len(getanalisis)>0:
                datos={'message':"success",'analisis':getanalisis}
            else:
                datos={'message':"analisis no encontrados"}
            return JsonResponse(datos)
    def post(self, request):
        jd=json.loads(request.body)
        analisis_nombre=jd.get('analisis_nombre')
        analisis_fregistro=jd.get('analisis_fregistro')
        analisis_estado=jd.get('analisis_estado')
        analisis.objects.create(analisis_nombre=analisis_nombre,analisis_fregistro=analisis_fregistro,analisis_estado=analisis_estado)
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd=json.loads(request.body)
        putanalisis=list(analisis.objects.filter(analisis_id=id).values())
        if len(putanalisis)>0:
            analisis_nombre=jd.get('analisis_nombre')
            analisis_fregistro=jd.get('analisis_fregistro')
            analisis_estado=jd.get('analisis_estado')
            analisis.objects.filter(analisis_id=id).update(analisis_nombre=analisis_nombre,analisis_fregistro=analisis_fregistro,analisis_estado=analisis_estado)
            datos={'message':"success"}
        else:
            datos={'message':"analisis no encontrados"}
        return JsonResponse(datos)
    
        
    
    def delete(self, request, id):
        delanalisis=list(analisis.objects.filter(analisis_id=id).values())
        if len(delanalisis)>0:
            analisis.objects.filter(analisis_id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"analisis no encontrados"}
        return JsonResponse(datos)
    
class especialidadView(View):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super().dispatch(request, *args, **kwargs)
        
        def get(self, request,id=0):
            if (id>0):
                getespecialidad=list(especialidad.objects.filter(especialidad_id=id).values())
                if len(getespecialidad)>0:
                    unespecialidad=getespecialidad[0];
                    datos={'message':"success",'especialidad':getespecialidad}
                else:
                    datos={'message':"especialidad no encontrados"}
                return JsonResponse(datos)
            else: 
                getespecialidad=list(especialidad.objects.values("especialidad_id","especialidad_nombre","especialidad_estado"))
                if len(getespecialidad)>0:
                    datos={'message':"success",'especialidad':getespecialidad}
                else:
                    datos={'message':"especialidad no encontrados"}
                return JsonResponse(datos)
            
        def post(self, request):
            jd=json.loads(request.body)
            especialidad_nombre=jd.get('especialidad_nombre')
            especialidad_estado=jd.get('especialidad_estado')
            especialidad.objects.create(especialidad_nombre=especialidad_nombre,especialidad_estado=especialidad_estado)
            datos={'message':"success"}
            return JsonResponse(datos)
        
        def put(self, request,id):
            jd=json.loads(request.body)
            putespecialidad=list(especialidad.objects.filter(especialidad_id=id).values())
            if len(putespecialidad)>0:
                especialidad_nombre=jd.get('especialidad_nombre')
                especialidad_estado=jd.get('especialidad_estado')
                especialidad.objects.filter(especialidad_id=id).update(especialidad_nombre=especialidad_nombre,especialidad_estado=especialidad_estado)
                datos={'message':"success"}
            else:
                datos={'message':"especialidad no encontrados"}
            return JsonResponse(datos)
        
        def delete(self, request, id):
            delespecialidad=list(especialidad.objects.filter(especialidad_id=id).values())
            if len(delespecialidad)>0:
                especialidad.objects.filter(especialidad_id=id).delete()
                datos={'message':"success"}
            else:
                datos={'message':"especialidad no encontrados"}
            return JsonResponse(datos)
        

class examenView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if (id>0):
            getexamen=list(examen.objects.filter(examen_id=id).values())
            if len(getexamen)>0:
                unexamen=getexamen[0];
                datos={'message':"success",'examen':getexamen}
            else:
                datos={'message':"examen no encontrados"}
            return JsonResponse(datos)
        else: 
            getexamen=list(examen.objects.values("examen_id","examen_nombre","examen_fregistro","examen_estado"))
            if len(getexamen)>0:
                datos={'message':"success",'examen':getexamen}
            else:
                datos={'message':"examen no encontrados"}
            return JsonResponse(datos)
        
    def post(self, request):
        jd=json.loads(request.body)
        examen_nombre=jd.get('examen_nombre')
        examen_fregistro=jd.get('examen_fregistro')
        examen_estado=jd.get('examen_estado')
        examen.objects.create(examen_nombre=examen_nombre,examen_fregistro=examen_fregistro,examen_estado=examen_estado)
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd=json.loads(request.body)
        putexamen=list(examen.objects.filter(examen_id=id).values())
        if len(putexamen)>0:
            examen_nombre=jd.get('examen_nombre')
            examen_fregistro=jd.get('examen_fregistro')
            examen_estado=jd.get('examen_estado')
            examen.objects.filter(examen_id=id).update(examen_nombre=examen_nombre,examen_fregistro=examen_fregistro,examen_estado=examen_estado)
            datos={'message':"success"}
        else:
            datos={'message':"examen no encontrados"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        delexamen=list(examen.objects.filter(examen_id=id).values())
        if len(delexamen)>0:
            examen.objects.filter(examen_id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"examen no encontrados"}
        return JsonResponse(datos)
    
class pacienteView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if (id>0):
            getpaciente=list(paciente.objects.filter(paciente_id=id).values())
            if len(getpaciente)>0:
                unpaciente=getpaciente[0];
                datos={'message':"success",'paciente':getpaciente}
            else:
                datos={'message':"paciente no encontrados"}
            return JsonResponse(datos)
        else: 
            getpaciente=list(paciente.objects.values("paciente_id","paciente_nombre","paciente_apellido","paciente_dni","paciente_fechanac","paciente_telefono","paciente_direccion","paciente_estado"))
            if len(getpaciente)>0:
                datos={'message':"success",'paciente':getpaciente}
            else:
                datos={'message':"paciente no encontrados"}
            return JsonResponse(datos)
        
    def post(self, request):
        jd=json.loads(request.body)
        paciente_nombre=jd.get('paciente_nombre')
        paciente_apellido=jd.get('paciente_apellido')
        paciente_dni=jd.get('paciente_dni')
        paciente_fechanac=jd.get('paciente_fechanac')
        paciente_telefono=jd.get('paciente_telefono')
        paciente_direccion=jd.get('paciente_direccion')
        paciente_estado=jd.get('paciente_estado')
        paciente.objects.create(paciente_nombre=paciente_nombre,paciente_apellido=paciente_apellido,paciente_dni=paciente_dni,paciente_fechanac=paciente_fechanac,paciente_telefono=paciente_telefono,paciente_direccion=paciente_direccion,paciente_estado=paciente_estado)
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd=json.loads(request.body)
        putpaciente=list(paciente.objects.filter(paciente_id=id).values())
        if len(putpaciente)>0:
            paciente_nombre=jd.get('paciente_nombre')
            paciente_apellido=jd.get('paciente_apellido')
            paciente_dni=jd.get('paciente_dni')
            paciente_fechanac=jd.get('paciente_fechanac')
            paciente_telefono=jd.get('paciente_telefono')
            paciente_direccion=jd.get('paciente_direccion')
            paciente_estado=jd.get('paciente_estado')
            paciente.objects.filter(paciente_id=id).update(paciente_nombre=paciente_nombre,paciente_apellido=paciente_apellido,paciente_dni=paciente_dni,paciente_fechanac=paciente_fechanac,paciente_telefono=paciente_telefono,paciente_direccion=paciente_direccion,paciente_estado=paciente_estado)
            datos={'message':"success"}
        else:
            datos={'message':"paciente no encontrados"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        delpaciente=list(paciente.objects.filter(paciente_id=id).values())
        if len(delpaciente)>0:
            paciente.objects.filter(paciente_id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"paciente no encontrados"}
        return JsonResponse(datos)
    
class medicoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if (id>0):
            getmedico=list(medico.objects.filter(medico_id=id).values())
            if len(getmedico)>0:
                unmedico=getmedico[0];
                datos={'message':"success",'medico':getmedico}
            else:
                datos={'message':"medico no encontrados"}
            return JsonResponse(datos)
        else: 
            getmedico=list(medico.objects.values("medico_id","medico_nombre","medico_apellido","medico_dni","medico_telefono","medico_direccion","medico_estado"))
            if len(getmedico)>0:
                datos={'message':"success",'medico':getmedico}
            else:
                datos={'message':"medico no encontrados"}
            return JsonResponse(datos)
        
    def post(self, request):
        jd=json.loads(request.body)
        medico_nombre=jd.get('medico_nombre')
        medico_apellido=jd.get('medico_apellido')
        medico_dni=jd.get('medico_dni')
        medico_telefono=jd.get('medico_telefono')
        medico_direccion=jd.get('medico_direccion')
        medico_estado=jd.get('medico_estado')
        medico.objects.create(medico_nombre=medico_nombre,medico_apellido=medico_apellido,medico_dni=medico_dni,medico_telefono=medico_telefono,medico_direccion=medico_direccion,medico_estado=medico_estado)
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd=json.loads(request.body)
        putmedico=list(medico.objects.filter(medico_id=id).values())
        if len(putmedico)>0:
            medico_nombre=jd.get('medico_nombre')
            medico_apellido=jd.get('medico_apellido')
            medico_dni=jd.get('medico_dni')
            medico_telefono=jd.get('medico_telefono')
            medico_direccion=jd.get('medico_direccion')
            medico_estado=jd.get('medico_estado')
            medico.objects.filter(medico_id=id).update(medico_nombre=medico_nombre,medico_apellido=medico_apellido,medico_dni=medico_dni,medico_telefono=medico_telefono,medico_direccion=medico_direccion,medico_estado=medico_estado)
            datos={'message':"success"}
        else:
            datos={'message':"medico no encontrados"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        delmedico=list(medico.objects.filter(medico_id=id).values())
        if len(delmedico)>0:
            medico.objects.filter(medico_id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"medico no encontrados"}
        return JsonResponse(datos)
    
class usuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if (id>0):
            getusuario=list(usuario.objects.filter(usuario_id=id).values())
            if len(getusuario)>0:
                unusuario=getusuario[0];
                datos={'message':"success",'usuario':getusuario}
            else:
                datos={'message':"usuario no encontrados"}
            return JsonResponse(datos)
        else: 
            getusuario=list(usuario.objects.values("usuario_id","usuario_nombre","usuario_apellido","usuario_dni","usuario_telefono","usuario_direccion","usuario_estado"))
            if len(getusuario)>0:
                datos={'message':"success",'usuario':getusuario}
            else:
                datos={'message':"usuario no encontrados"}
            return JsonResponse(datos)
        
    def post(self, request):
        jd=json.loads(request.body)
        usuario_nombre=jd.get('usuario_nombre')
        usuario_apellido=jd.get('usuario_apellido')
        usuario_dni=jd.get('usuario_dni')
        usuario_telefono=jd.get('usuario_telefono')
        usuario_direccion=jd.get('usuario_direccion')
        usuario_estado=jd.get('usuario_estado')
        usuario.objects.create(usuario_nombre=usuario_nombre,usuario_apellido=usuario_apellido,usuario_dni=usuario_dni,usuario_telefono=usuario_telefono,usuario_direccion=usuario_direccion,usuario_estado=usuario_estado)
        datos={'message':"success"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd=json.loads(request.body)
        putusuario=list(usuario.objects.filter(usuario_id=id).values())
        if len(putusuario)>0:
            usuario_nombre=jd.get('usuario_nombre')
            usuario_apellido=jd.get('usuario_apellido')
            usuario_dni=jd.get('usuario_dni')
            usuario_telefono=jd.get('usuario_telefono')
            usuario_direccion=jd.get('usuario_direccion')
            usuario_estado=jd.get('usuario_estado')
            usuario.objects.filter(usuario_id=id).update(usuario_nombre=usuario_nombre,usuario_apellido=usuario_apellido,usuario_dni=usuario_dni,usuario_telefono=usuario_telefono,usuario_direccion=usuario_direccion,usuario_estado=usuario_estado)
            datos={'message':"success"}
        else:
            datos={'message':"usuario no encontrados"}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        delusuario=list(usuario.objects.filter(usuario_id=id).values())
        if len(delusuario)>0:
            usuario.objects.filter(usuario_id=id).delete()
            datos={'message':"success"}
        else:
            datos={'message':"usuario no encontrados"}
        return JsonResponse(datos)
    
# class realizar_examenView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
#     def get(self, request,id=0):
#         if (id>0):
#             getrealizar_examen=list(realizar_examen.objects.filter(realizar_examen_id=id).values())
#             if len(getrealizar_examen)>0:
#                 unrealizar_examen=getrealizar_examen[0];
#                 datos={'message':"success",'realizar_examen':getrealizar_examen}
#             else:
#                 datos={'message':"realizar_examen no encontrados"}
#             return JsonResponse(datos)
#         else: 
#             getrealizar_examen=list(realizar_examen.objects.values("realizar_examen_id","realizar_examen_fecha","realizar_examen_hora","realizar_examen_estado"))
#             if len(getrealizar_examen)>0:
#                 datos={'message':"success",'realizar_examen':getrealizar_examen}
#             else:
#                 datos={'message':"realizar_examen no encontrados"}
#             return JsonResponse(datos)
        
#     def post(self, request):
#         jb=json.loads(request.body)
#         realizar_examen_fecha=jb.get('realizar_examen_fecha')
#         realizar_examen_hora=jb.get('realizar_examen_hora')
#         realizar_examen_estado=jb.get('realizar_examen_estado')
#         realizar_examen.objects.create(realizar_examen_fecha=realizar_examen_fecha,realizar_examen_hora=realizar_examen_hora,realizar_examen_estado=realizar_examen_estado)
#         datos={'message':"success"}
#         return JsonResponse(datos)
    
#     def put(self, request,id):
#         jb=json.loads(request.body)
#         putrealizar_examen=list(realizar_examen.objects.filter(realizar_examen_id=id).values())
#         if len(putrealizar_examen)>0:
#             realizar_examen_fecha=jb.get('realizar_examen_fecha')
#             realizar_examen_hora=jb.get('realizar_examen_hora')
#             realizar_examen_estado=jb.get('realizar_examen_estado')
#             realizar_examen.objects.filter(realizar_examen_id=id).update(realizar_examen_fecha=realizar_examen_fecha,realizar_examen_hora=realizar_examen_hora,realizar_examen_estado=realizar_examen_estado)
#             datos={'message':"success"}
#         else:
#             datos={'message':"realizar_examen no encontrados"}
#         return JsonResponse(datos)
    
#     def delete(self, request, id):
#         delrealizar_examen=list(realizar_examen.objects.filter(realizar_examen_id=id).values())
#         if len(delrealizar_examen)>0:
#             realizar_examen.objects.filter(realizar_examen_id=id).delete()
#             datos={'message':"success"}
#         else:
#             datos={'message':"realizar_examen no encontrados"}
#         return JsonResponse(datos)
    
