from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
from bot.models import UsuarioTelegram, Texto, Imagem, Documento

now = datetime.now()


class Command(BaseCommand):
    updater = Updater('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

    def start(bot, update):
        update.message.reply_text('Ola {}, bem vindo ao nosso Bot de comunicação'.format(
            update.message.from_user.first_name))
        update.message.reply_text(
            'Seu código de acesso é {}'.format(update.message.from_user.id))
        update.message.reply_text('Favor Cadastrar em nosso sistema ')

    def photo_list(bot, update):
        nomes = UsuarioTelegram.objects.all()
        user = update.message.from_user.first_name
        photo_file = bot.getFile(update.message.photo[-1].file_id)

        for a in nomes:
            if a.nome == user:
                Imagem.objects.create(usuario=a, imagem=photo_file.download())
        print('imagem enviada')
        update.message.reply_text('Foto enviada para o sistema ')

    def doc_list(bot, update):
        nomes = UsuarioTelegram.objects.all()
        user = update.message.from_user.first_name
        doc_file = bot.getFile(update.message.document.file_id)
        for a in nomes:
            if a.nome == user:
                Documento.objects.create(usuario=a, documento=doc_file.download(custom_path='/media/'))
        print('Doc enviado')
        update.message.reply_text('Documento enviado para o sistema ')

    def chat_listener(bot, update):
        nomes = UsuarioTelegram.objects.all()
        text = update.message.text
        user = update.message.from_user.first_name
        userid = update.message.from_user.id
        date = str(update.message.date)
        ide = str(update.message.chat_id)

        for a in nomes:
            if a.nome == user:
                Texto.objects.create(usuario=a, texto=text)

        print('{0} {1}:{2} {3}  .... {4}'.format(
            date, user, text, ide, userid))

    unknown_handler = MessageHandler(Filters.text, chat_listener)
    updater.dispatcher.add_handler(unknown_handler)

    handler = MessageHandler(Filters.photo, photo_list)
    updater.dispatcher.add_handler(handler)

    handlers = MessageHandler(Filters.document, doc_list)
    updater.dispatcher.add_handler(handlers)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
