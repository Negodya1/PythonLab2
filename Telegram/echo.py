from telegram.ext import Updater, MessageHandler, Filters


def echo(update, context):
    update.message.reply_text("Я получил сообщение " + update.message.text)
    print(update.message.from_user)


def main():
    updater = Updater("5335234442:AAGMABLSsEPpeTn22wYyKtLRYE6jNYr0ZaU", use_context=True)

    dp = updater.dispatcher

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()