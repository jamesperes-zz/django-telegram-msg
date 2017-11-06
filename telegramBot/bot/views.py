from django.shortcuts import render
import telepot
from django.http import HttpResponseRedirect
from .models import *

bot = telepot.Bot('token here!!')

# Create your views here.


def pagina_envio(request):
    if request.method == 'GET':
        user_located = UserTelegram.objects.all()
        return render(request, 'bot/index.html', {'users': user_located})

    elif request.method == 'POST':
        post_file = request.FILES.get('post_file')
        if post_file:
            user_post = request.POST.get('user')
            extension = post_file.name[post_file.name.rfind('.'):]
            if extension in ('.jpg', '.png', '.jpeg', '.gif'):
                bot.sendPhoto(user_post, post_file)
            else:
                bot.sendDocument(user_post, post_file)

        message = request.POST.get('message')
        if message:
            user_post = request.POST.get('user')
            bot.sendMessage(user_post, message)
        return HttpResponseRedirect('/')


def list_user(request):
    users = UserTelegram.objects.all()
    return render(request, 'bot/users.html', {'users': users})


def texthistory(request, user_id):
    user = UserTelegram.objects.get(id=user_id)
    text = Text.objects.filter(user_id=user_id)
    return render(request, 'bot/texthistory.html', {'user': user, 
                                                    'text': text})


def photohistory(request, user_id):
    user = UserTelegram.objects.get(id=user_id)
    image = Image.objects.filter(user_id=user_id)
    return render(request, 'bot/photohistory.html', {'user': user,
                                                     'image': image})
