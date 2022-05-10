from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import numpy as np


reply_keyboard = [['/Dice', '/Timer']]
reply_keyboard2 = [['D6', '2xD6'], ['D20', 'Назад']]
reply_keyboard3 = [['30 секунд', '1 минута'], ['5 минут', 'Назад']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=False)

def tg_start(update, context):
    update.message.reply_text(
        "Я бот-помощник для настольных игр. Я могу бросать кости и засекать время",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        reply_markup=ReplyKeyboardRemove()
    )


def dice(update, context):
    update.message.reply_text(
        "Какие кости желаете бросить?",
        reply_markup=markup2
    )


def timer(update, context):
    update.message.reply_text(
        "Сколько времени засечь?",
        reply_markup=markup3
    )


def echo(update, context):
    text = str(update.message.text)
    if 'назад' in text.lower():
        update.message.reply_text(
            "Бросить кости или засечь время?",
            reply_markup=markup
        )
    elif 'D' in text:
        text = str(update.message.text)
        dpos = text.find('D')
        xpos = dpos
        if 'x' in text:
            xpos = text.find('x')
        quantity = 1
        if xpos > 0:
            quantity = int(text[0:xpos])

        dicetype = int(text[dpos + 1:])

        res = "Результат броска: "
        multi = False
        intres = 0
        if quantity > 1:
            multi = True
        while quantity > 0:
            roll = np.random.randint(1, dicetype + 1)
            intres += roll
            res += str(roll) + ' '
            if quantity > 1:
                res += "+ "
            quantity -= 1
        if multi:
            res += "= " + str(intres)
        update.message.reply_text(res)
    elif 'сек' in text.lower() or 'мин' in text.lower():
        chat_id = update.message.chat_id

        seconds = 0
        if 'сек' in text.lower():
            cpos = text.lower().find('с')
            seconds = int(text[:cpos])
        else:
            mpos = text.lower().find('м')
            seconds += int(text[:mpos]) * 60

        due = int(seconds)
        if due < 0:
            return

        new_job = context.job_queue.run_once(task, due, context=chat_id)
        context.chat_data['job'] = new_job
        update.message.reply_text(f'Засёк время. Напишу через {due} секунд')


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Время вышло')


def main():
    updater = Updater("5335234442:AAGMABLSsEPpeTn22wYyKtLRYE6jNYr0ZaU", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    dp.add_handler(CommandHandler("Dice", dice))
    dp.add_handler(CommandHandler("Timer", timer))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()