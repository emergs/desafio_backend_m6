from django.db import models


class FileUpload(models.Model):
    file_parser = models.FileField(upload_to="storeged_file")


class FileParserModel(models.Model):
    tipo = models.CharField(max_length=15)
    data = models.CharField(max_length=8)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=10)
    dono_da_loja = models.CharField(max_length=20)
    nome_da_loja = models.CharField(max_length=20)
