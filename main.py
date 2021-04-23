from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils import helpers
import os

reply_keyboard = [['/textbook', '/tests']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def textbook_1(update, context):
    bot = context.bot
    names = os.listdir('themes')
    update.message.reply_text(
        "СПРАВОЧНИК",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=names[0], callback_data='parts-of-speech')],
            [InlineKeyboardButton(text=names[1], callback_data='phonetics')],
            [InlineKeyboardButton(text=names[2], callback_data='grammar')],
            [InlineKeyboardButton(text=names[3], callback_data='lexis')],
            [InlineKeyboardButton(text=names[4], callback_data='punctuation')],
            [InlineKeyboardButton(text=names[5], callback_data='particles-and-conjunctions')],
            [InlineKeyboardButton(text=names[6], callback_data='orphography')]]
        ),
    )


def in_parts_of_speech(update, context):
    update.callback_query.message.reply_text('----------------------------')
    names = os.listdir(os.path.join('themes', '1) Части речи'))
    update.callback_query.message.reply_text(
        'Части речи',
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text=names[0], callback_data='noun')],
            [InlineKeyboardButton(text=names[1], callback_data='verb')]]
        ),
    )


def in_noun():
    names = os.listdir(os.path.join('themes', '1) Части речи', '1) Существительное'))
    f = open('example.txt', 'r')
    pass


def in_verb():
    pass


# --------------------------------------------------------------------------------


def in_phonetics(update, context):
    update.callback_query.answer('В разработке')


def in_grammar(update, context):
    update.callback_query.answer('В разработке')


def in_lexis(update, context):
    update.callback_query.answer('В разработке')


def in_punctuation(update, context):
    update.callback_query.answer('В разработке')


def in_particles_and_conjunctions(update, context):
    update.callback_query.answer('В разработке')


def in_orphography(update, context):
    update.callback_query.answer('В разработке')


def start(update, context):
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )
    print('Done!')


def main():
    token = '1797940789:AAENadc1txh59h5FX3Kd_DMUrBECpiYwu9g'

    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("textbook", textbook_1))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))

    files = os.listdir('themes')

    dp.add_handler(CallbackQueryHandler(in_parts_of_speech, pattern='parts-of-speech'))
    dp.add_handler(CallbackQueryHandler(in_phonetics, pattern='phonetics'))
    dp.add_handler(CallbackQueryHandler(in_grammar, pattern='grammar'))
    dp.add_handler(CallbackQueryHandler(in_lexis, pattern='lexis'))
    dp.add_handler(CallbackQueryHandler(in_punctuation, pattern='punctuation'))
    dp.add_handler(CallbackQueryHandler(in_particles_and_conjunctions, pattern='particles-and-conjunctions'))
    dp.add_handler(CallbackQueryHandler(in_orphography, pattern='orphography'))

    dp.add_handler(CallbackQueryHandler(in_noun, pattern='noun'))
    dp.add_handler(CallbackQueryHandler(in_verb, pattern='verb'))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
