from django.db import models


class UsuarioTelegram(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Texto(models.Model):
    usuario = models.ForeignKey(UsuarioTelegram)
    texto = models.TextField()


class Imagem(models.Model):
    usuario = models.ForeignKey(UsuarioTelegram)
    imagem = models.ImageField(upload_to='uploads')


class Documento(models.Model):
    usuario = models.ForeignKey(UsuarioTelegram)
    documento = models.FileField(upload_to='uploads')

