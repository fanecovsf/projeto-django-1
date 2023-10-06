from django.db import models

class Endereco(models.Model):

    id_endereco=models.AutoField(primary_key=True)
    rua=models.CharField(max_length=150,blank=False,null=False)
    numero=models.IntegerField(blank=False,null=False)
    cep=models.IntegerField(blank=False,null=False)


class Residente(models.Model):

    id_residente=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=100,blank=False,null=False)
    sobrenome=models.CharField(max_length=100,blank=False,null=False)
    idade=models.IntegerField(blank=False,null=False)
    email=models.CharField(max_length=150,blank=False,null=False)


    def __str__(self) -> str:
        return self.id_residente


    def __str__(self) -> str:
        return self.id_endereço