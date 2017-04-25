from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
from bot.models import UsuarioTelegram, Texto

now = datetime.now()


class Command(BaseCommand):
    updater = Updater('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

    def start(bot, update):
        update.message.reply_text('Ola {}, bem vindo ao nosso Bot de comunicação'.format(
            update.message.from_user.first_name))
        update.message.reply_text(
            'Seu código de acesso é {}'.format(update.message.from_user.id))
        update.message.reply_text('Favor Cadastrar em nosso sistema ')

    def chat_listener(bot, update):

        text = update.message.text
        user = update.message.from_user.first_name
        userid = update.message.from_user.id
        date = str(update.message.date)
        ide = str(update.message.chat_id)

        nomes = UsuarioTelegram.objects.all()

        for a in nomes:
            if a.nome == user:
                Texto.objects.create(usuario=a, texto=text)

        print('{0} {1}:{2} {3}  .... {4}'.format(
            date, user, text, ide, userid))

    unknown_handler = MessageHandler(Filters.text, chat_listener)
    updater.dispatcher.add_handler(unknown_handler)
    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
