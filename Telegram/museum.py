from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


reply_keyboard = [['2', 'Выход']]
reply_keyboard2 = [['3']]
reply_keyboard3 = [['1', '4']]
reply_keyboard4 = [['1']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=True)
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=True)

def tg_start(update, context):
    update.message.reply_text(
        "Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!\nВ данном зале представлены картины известного художника-авангардиста, Казимира Малевича\nОтсюда можно попасть во второй зал, посвещённый скульптуре",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        reply_markup=ReplyKeyboardRemove()
    )


def echo(update, context):
    if update.message.text == '1':
        update.message.reply_text(
            "В данном зале представлены картины известного художника-авангардиста, Казимира Малевича\nОтсюда можно попасть во второй зал, посвящённый скульптуре",
            reply_markup=markup
        )
    elif update.message.text == '2':
        update.message.reply_text(
            "В данном зале представлены скульптуры Марка Антокольского\nОтсюда можно попасть в третий зал, посвящённый народным музыкальным инструментам",
            reply_markup=markup2
        )
    elif update.message.text == '3':
        update.message.reply_text(
            "В данном зале представлены народные музыкальные инструменты племён, проживавших на территории Кемеровской области в 7 веке\nОтсюда можно попасть в первый зал, посвящённый изобразительному исскуству\nИли в четвёртый зал, посвящённый памяти Великой Отечетсвенной Войны",
            reply_markup=markup3
        )
    elif update.message.text == '4':
        update.message.reply_text(
            "В данном зале представлены артефакты времён Великой Отечественной Войны\nОтсюда можно попасть в первый зал, посвящённый изобразительному исскуству",
            reply_markup=markup4
        )
    elif update.message.text == 'Выход':
        update.message.reply_text(
            "«Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!",
        )

def main():
    updater = Updater("5335234442:AAGMABLSsEPpeTn22wYyKtLRYE6jNYr0ZaU", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()