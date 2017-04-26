"""telegramBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bot.views import pagina_envio, lista_usuario, usuario, usuario_foto
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
    url(r'^$', pagina_envio),
    url(r'^usuarios/$', lista_usuario, name='lista_usuario'),
    url(r'^usuario/(?P<usuario_id>[0-9]+)$', usuario),
    url(r'^usuariofoto/(?P<usuario_id>[0-9]+)$', usuario_foto, name='usuario_foto'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
