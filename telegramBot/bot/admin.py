from django.contrib import admin
from .models import UsuarioTelegram, Imagem


class UsuarioTelegramAdmin(admin.ModelAdmin):
    pass


class ImagemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Imagem, ImagemAdmin)
admin.site.register(UsuarioTelegram, UsuarioTelegramAdmin)
