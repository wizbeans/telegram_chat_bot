import logging
from telegram.ext import *
import responses

API_KEY = 'donot_copy_my_key'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('hello this is the starting of your chat with maggi!')


def help_command(update, context):
    update.message.reply_text('Try typing anything and it will depend on my mood to respond')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling(1.0)
    updater.idle()
