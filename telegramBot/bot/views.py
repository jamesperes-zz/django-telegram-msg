from django.shortcuts import render
import telepot
from django.http import HttpResponseRedirect
from .models import UsuarioTelegram

bot = telepot.Bot('----TOKEN AQUI----')

# Create your views here.


def pagina_envio(request):
    if request.method == 'GET':
        usuario_localizados = UsuarioTelegram.objects.all()
        return render(request, 'bot/index.html', {'usuarios': usuario_localizados})

    elif request.method == 'POST':
        arquivo = request.FILES.get('arquivo')
        if arquivo:
            usuario_post = request.POST.get('usuario')
            extension = arquivo.name[arquivo.name.rfind('.'):]
            if extension in ('.jpg', '.png', '.jpeg', '.gif'):
                bot.sendPhoto(usuario_post, arquivo)
            else:
                bot.sendDocument(usuario_post, arquivo)
        
        mensagem = request.POST.get('mensagem')
        if mensagem:
            usuario_post = request.POST.get('usuario')
            bot.sendMessage(usuario_post, mensagem)
        return HttpResponseRedirect('/')
