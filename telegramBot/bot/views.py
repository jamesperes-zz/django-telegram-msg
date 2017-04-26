from django.shortcuts import render
import telepot
from django.http import HttpResponseRedirect
from .models import UsuarioTelegram, Imagem, Texto

bot = telepot.Bot('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

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


def lista_usuario(request):
    usuarios = UsuarioTelegram.objects.all()
    return render(request, 'bot/usuarios.html', {'usuarios': usuarios})


def usuario(request, usuario_id):
    usuario = UsuarioTelegram.objects.get(id=usuario_id)
    texto = Texto.objects.filter(usuario_id=usuario_id)
    return render(request, 'bot/usuario.html', {'usuario': usuario,
                                                                         'texto':texto})

def usuario_foto(request, usuario_id):
    usuario = UsuarioTelegram.objects.get(id=usuario_id)
    imagem = Imagem.objects.filter(usuario_id=usuario_id)
    return render(request, 'bot/usuariofoto.html', {'usuario': usuario,
                                                                                'imagem':imagem})