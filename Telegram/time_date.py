from telegram.ext import Updater, CommandHandler, Filters
import time


def tg_start(update, context):
    update.message.reply_text("Привет! Я время-бот.\n/time для получения текущего времени.\n/date для получения текущей даты.")


def tg_help(update, context):
    update.message.reply_text("/time для получения текущего времени.\n/date для получения текущей даты.")


def tg_time(update, context):
    tup = time.asctime()
    update.message.reply_text("Текущее время: " + tup[11:19])


def tg_date(update, context):
    tup = time.asctime()
    update.message.reply_text("Текущая дата: " + tup[8:10] + ' ' + tup[4:7] + ' ' + tup[19:24])


def main():
    updater = Updater("5335234442:AAGMABLSsEPpeTn22wYyKtLRYE6jNYr0ZaU", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("help", tg_help))
    dp.add_handler(CommandHandler("time", tg_time))
    dp.add_handler(CommandHandler("date", tg_date))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()