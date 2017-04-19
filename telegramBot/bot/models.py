from django.db import models

class UsuarioTelegram(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
