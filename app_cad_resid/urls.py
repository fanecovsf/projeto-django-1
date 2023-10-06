from django.urls import path

from app_cad_resid.views import EnderecoAPI, EnderecoDetailsAPI
from app_cad_resid.views import ResidenteAPI, ResidenteDetailsAPI

urlpatterns = [
    path('endereco/', EnderecoAPI.as_view(), name='enderecos_all'),
    path('residente/', ResidenteAPI.as_view(), name='residentes_all'),
    path('endereco/<id_endereco>', EnderecoDetailsAPI.as_view(), name='enderecos_details'),
    path('residente/<id_residente>', EnderecoDetailsAPI.as_view(), name='residentes_details'),
]