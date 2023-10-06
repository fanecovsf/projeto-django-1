from django.shortcuts import render
from .models import Endereco
from .models import Residente

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app_cad_resid.services import EnderecoServices
from app_cad_resid.services import ResidenteServices

from app_cad_resid.serializers import ResidenteSerializer
from app_cad_resid.serializers import ResidenteSerializer

class EnderecoAPI(APIView):

    def get(self,request):
        enderecos=EnderecoServices.query_all()
        serializer=ResidenteSerializer(enderecos,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data
        serializer=ResidenteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class EnderecoDetailsAPI(APIView):
    
    def get(self,request,id_endereco):
        endereco=EnderecoServices.get(id_endereco)

        if endereco:
            serializer=ResidenteSerializer(endereco)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'Endereco nao existe'},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id_endereco):
        endereco=EnderecoServices.get(id_endereco)

        if endereco:
            endereco.delete()
            return Response(data={'Delete':'Endereco deletado'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'Erro':'Endereco nao existe'},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id_endereco):
        data=request.data
        endereco=EnderecoServices.get(id_endereco)

        if endereco:
            serializer=ResidenteSerializer(instance=endereco,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'Erro':'Endereco nao existe'},status=status.HTTP_404_NOT_FOUND)
    

class ResidenteAPI(APIView):

    def get(self,request):
        residente=ResidenteServices.query_all()
        serializer=ResidenteSerializer(residente,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        data=request.data
        serializer=ResidenteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class ResidenteDetailsAPI(APIView):
    
    def get(self,request,id_residente):
        residente=ResidenteServices.get(id_residente)

        if residente:
            serializer=ResidenteSerializer(residente)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'Residente nao existe'},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id_residente):
        residente=ResidenteServices.get(id_residente)

        if residente:
            residente.delete()
            return Response(data={'Delete':'Residente deletado'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'Erro':'Residente nao existe'},status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,id_residente):
        data=request.data
        residente=ResidenteServices.get(id_residente)

        if residente:
            serializer=ResidenteSerializer(instance=residente,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'Erro':'Residente nao existe'},status=status.HTTP_404_NOT_FOUND)
        

