from django.contrib import admin
from .models import UsuarioTelegram


class UsuarioTelegramAdmin(admin.ModelAdmin):
    pass

admin.site.register(UsuarioTelegram, UsuarioTelegramAdmin)
