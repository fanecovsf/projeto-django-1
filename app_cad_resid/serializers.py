from app_cad_resid.models import Endereco
from app_cad_resid.models import Residente 

from rest_framework import serializers

class ResidenteSerializer(serializers.ModelSerializer):

    class Meta:
        model=Endereco
        fields='__all__'

class ResidenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Residente
        fields='__all__'


