from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
from bot.models import UserTelegram, Text, Image, Document
import os
from os.path import basename
from django.core.files import File
import tempfile

now = datetime.now()
tmp = tempfile.gettempdir()


def upload(user, telegramfile, model, modelfield):
    name = basename(telegramfile.file_path)
    path_file = os.path.join(tmp, name)
    telegramfile.download(custom_path=path_file)
    obj = model(user=user)
    getattr(obj, modelfield).save(
        os.path.basename(path_file),
        File(open(path_file, 'rb')))
    obj.save()
    os.remove(path_file)


class Command(BaseCommand):
    updater = Updater('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

    def start(bot, update):
        update.message.reply_text('Ola {}, bem vindo ao nosso Bot de comunicação'.format(
            update.message.from_user.first_name))
        update.message.reply_text(
            'Seu código de acesso é {}'.format(update.message.from_user.id))
        update.message.reply_text('Favor Cadastrar em nosso sistema ')

    def photo_list(bot, update):
        names = UserTelegram.objects.all()
        user = update.message.from_user.first_name
        photo_file = bot.getFile(update.message.photo[-1].file_id)

        for a in names:
            if a.name == user:
                try:
                    upload(a, photo_file, Image, 'image_file')
                except Exception as error:
                    print('Falha de upload', error)
        print('imagem enviada')
        update.message.reply_text('Foto enviada para o sistema ')

    def doc_list(bot, update):
        names = UserTelegram.objects.all()
        user = update.message.from_user.first_name
        doc_file = bot.getFile(update.message.document.file_id)
        for a in names:
            if a.name == user:
                try:
                    upload(a, doc_file, Document, 'document_file')
                except Exception as error:
                    print('Falha de upload', error)
        print('Doc enviado')
        update.message.reply_text('Documento enviado para o sistema ')

    def chat_listener(bot, update):
        names = UserTelegram.objects.all()
        text = update.message.text
        user = update.message.from_user.first_name
        userid = update.message.from_user.id
        date = str(update.message.date)
        ide = str(update.message.chat_id)

        for a in names:
            if a.name == user:
                Text.objects.create(user=a, text_file=text)

        print('{0} {1}:{2} {3}  .... {4}'.format(
            date, user, text, ide, userid))
        print()
    unknown_handler = MessageHandler(Filters.text, chat_listener)
    updater.dispatcher.add_handler(unknown_handler)

    handler = MessageHandler(Filters.photo, photo_list)
    updater.dispatcher.add_handler(handler)

    handlers = MessageHandler(Filters.document, doc_list)
    updater.dispatcher.add_handler(handlers)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
