from django.shortcuts import render
import telepot
from django.http import HttpResponseRedirect
from .models import UsuarioTelegram

bot = telepot.Bot('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

# Create your views here.


def pagina_envio(request):
    if request.method == 'GET':
        usuario_localizados = UsuarioTelegram.objects.all()
        return render(request, 'bot/index.html', {'usuarios': usuario_localizados})

    elif request.method == 'POST':
        usuario_post = request.POST.get('usuario', None)
        messagem_post = request.POST.get('mensagem', None)
        bot.sendMessage(usuario_post, messagem_post)
        return HttpResponseRedirect('/')
