from app_cad_resid.models import Endereco
from app_cad_resid.models import Residente

class EnderecoServices:

    @staticmethod
    def get(id_endereco):
        try:
            endereço= Endereco.objects.get(id_endereço=id_endereco)
            return endereço
        except:
            return None

    @staticmethod
    def query_all():
        enderecos=Endereco.objects.all()
        return enderecos    
        

class ResidenteServices:

    @staticmethod
    def get(id_residente):
        try:
            residente=Residente.objects.get(id_residente=id_residente)
            return residente
        except:
            return None
        

    @staticmethod
    def query_all():
        residente=Residente.objects.all()
        return residente