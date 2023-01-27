from django.db import models

class UploadFile(models.Model):
    cnab_file = models.FileField(upload_to="uploads")


class FileParserModel(models.Model):
    tipo = models.CharField(max_length=13)
    data = models.CharField(max_length=8)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=8)
    dono = models.CharField(max_length=14)
    loja = models.CharField(max_length=19)

