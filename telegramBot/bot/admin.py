from django.contrib import admin
from .models import *


class UserTelegramAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
admin.site.register(UserTelegram, UserTelegramAdmin)
