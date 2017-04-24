from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler
from datetime import datetime

now = datetime.now()

class Command(BaseCommand):
    def start(bot, update):
        update.message.reply_text('Ola {}, bem vindo ao nosso Bot de comunicação'.format(update.message.from_user.first_name))
        update.message.reply_text('Seu código de acesso é {}'.format(update.message.from_user.id))
        update.message.reply_text('Favor Cadastrar em nosso sistema ')


    updater = Updater('-------TOKEN AQUI---------')

    updater.dispatcher.add_handler(CommandHandler('start', start))


    updater.start_polling()
    updater.idle()
