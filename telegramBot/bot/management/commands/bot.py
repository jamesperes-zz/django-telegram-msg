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
    updater = Updater('TOKEN HERE!!')

    def start(bot, update):
        update.message.reply_text('Hello {}, Wellcome the Bot '.format(
            update.message.from_user.first_name))
        update.message.reply_text(
            'Your code is {}'.format(update.message.from_user.id))
        update.message.reply_text('Please, register your code and first name in system')

    def photo_list(bot, update):
        names = UserTelegram.objects.all()
        user = update.message.from_user.first_name
        photo_file = bot.getFile(update.message.photo[-1].file_id)
        for a in names:
            if a.name == user:
                try:
                    upload(a, photo_file, Image, 'image_file')
                except Exception as error:
                    print('Fail ', error)
        print('Photo upload completed')
        update.message.reply_text('Photo upload completed ')

    def doc_list(bot, update):
        names = UserTelegram.objects.all()
        user = update.message.from_user.first_name
        doc_file = bot.getFile(update.message.document.file_id)
        for a in names:
            if a.name == user:
                try:
                    upload(a, doc_file, Document, 'document_file')
                except Exception as error:
                    print('Fail ', error)
        print('Doc upload completed')
        update.message.reply_text('Doc upload completed ')

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

    text_handler = MessageHandler(Filters.text, chat_listener)
    updater.dispatcher.add_handler(text_handler)

    photo_handler = MessageHandler(Filters.photo, photo_list)
    updater.dispatcher.add_handler(photo_handler)

    doc_handler = MessageHandler(Filters.document, doc_list)
    updater.dispatcher.add_handler(doc_handler)

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
