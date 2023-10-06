from django.shortcuts import render
from .models import Endereco
from .models import Residente

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_cad_resid.services import EnderecoServices
from app_cad_resid.services import ResidenteServices

from app_cad_resid.serializers import EnderecoSerializer
from app_cad_resid.serializers import ResidenteSerializer

from projeto_cad_resid.abstract import AbstractAPIView

class EnderecoAPI(AbstractAPIView):
    model_serializer=EnderecoSerializer
    model_service=EnderecoServices

        
class EnderecoDetailsAPI(APIView):
    
    def get(self,request,id):
        endereco=EnderecoServices.get(id)

        if endereco:
            serializer=EnderecoSerializer(endereco)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'Endereco nao existe'},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        endereco=EnderecoServices.get(id)

        if endereco:
            endereco.delete()
            return Response(data={'Delete':'Endereco deletado'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'Erro':'Endereco nao existe'},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        data=request.data
        endereco=EnderecoServices.get(id)

        if endereco:
            serializer=EnderecoSerializer(instance=endereco,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'Erro':'Endereco nao existe'},status=status.HTTP_404_NOT_FOUND)
    

class ResidenteAPI(AbstractAPIView):
    model_serializer=ResidenteSerializer
    model_service=ResidenteServices
        

class ResidenteDetailsAPI(APIView):
    
    def get(self,request,id):
        residente=ResidenteServices.get(id)

        if residente:
            serializer=ResidenteSerializer(residente)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'Residente nao existe'},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        residente=ResidenteServices.get(id)

        if residente:
            residente.delete()
            return Response(data={'Delete':'Residente deletado'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'Erro':'Residente nao existe'},status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,id):
        data=request.data
        residente=ResidenteServices.get(id)

        if residente:
            serializer=ResidenteSerializer(instance=residente,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'Erro':'Residente nao existe'},status=status.HTTP_404_NOT_FOUND)
        

