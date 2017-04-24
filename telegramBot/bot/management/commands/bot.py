from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler
from datetime import datetime

now = datetime.now()

class Command(BaseCommand):
    def start(bot, update):
        update.message.reply_text('Ola {}, bem vindo ao nosso Bot de comunicação'.format(update.message.from_user.first_name))
        update.message.reply_text('Seu código de acesso é {}'.format(update.message.from_user.id))
        update.message.reply_text('Favor Cadastrar em nosso sistema ')

    def hello(bot, update):
        update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))


    def hora(bot, update):
        update.message.reply_text(
            'horas {}:{} : {}'.format(now.hour, now.minute, now))

    updater = Updater('228843118:AAGk6hkBpjIW_DazSEv843WwD_SMCuOFS0M')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('hora', hora))

    updater.start_polling()
    updater.idle()
