from rest_framework import serializers
from rest_framework import viewsets, routers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Coor_Carrera, Coor_Institucionales, Otras_Comisiones
from .models import BolsaEmpleo
from .serializers import  Coor_Carrera_Serializer, Coor_Institucionales_Serializer, Otras_comisiones_Serializer
from . serializers import Bolsa_empleo_Serializer

from .models import DependenciasInstitucionales
from .serializers import DependenciasInstitucionales_Serializer

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def listCoordinaciones_carrera(request):
    carrera = Coor_Carrera.objects.filter().order_by('id') 
    serializer = Coor_Carrera_Serializer(carrera, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listCoordinaciones_institucionales(request):
    coor_inst = Coor_Institucionales.objects.filter().order_by('id') 
    serializer = Coor_Institucionales_Serializer(coor_inst, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_otras_comisiones(request):
    otras = Otras_Comisiones.objects.filter().order_by('id') 
    serializer = Otras_comisiones_Serializer(otras, many=True)
    return Response(serializer.data)



class BolsaEmpleo_ViewSet(viewsets.ModelViewSet):
    queryset = BolsaEmpleo.objects.all().order_by('-id')
    serializer_class = Bolsa_empleo_Serializer
    router = routers.DefaultRouter()
#router.register(r'bolsaEmpleo', BolsaEmpleo_ViewSet)


@api_view(['GET'])
def listBolsaEmpleoPublic(request):
    lista = BolsaEmpleo.objects.filter().order_by('-id') 
    serializer = Bolsa_empleo_Serializer(lista, many=True)
    return Response(serializer.data)

## DEPENDENCIAS

class DependenciasInstitucionales_ViewSet(viewsets.ModelViewSet):
    queryset = DependenciasInstitucionales.objects.all().order_by('-id')
    serializer_class = DependenciasInstitucionales_Serializer
router = routers.DefaultRouter()

