from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove
from telegram.utils import helpers

# Напишем соответствующие функции.
reply_keyboard = [['/textbook', '/tests']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def textbook(update, context):
    bot = context.bot
    url_parts_of_speech = helpers.create_deep_linked_url(bot.username, 'parts-of-speech')
    url_phonetics = helpers.create_deep_linked_url(bot.username, 'phonetics')
    url_grammar = helpers.create_deep_linked_url(bot.username, 'grammar')
    url_lexis = helpers.create_deep_linked_url(bot.username, 'lexis')
    url_punctuation = helpers.create_deep_linked_url(bot.username, 'punctuation')
    url_particles_and_conjunctions = helpers.create_deep_linked_url(bot.username, 'particles-and-conjunctions')
    url_orphography = helpers.create_deep_linked_url(bot.username, 'orphography')
    text = f'''Справочник:
        
    [Части речи]({url_parts_of_speech})
    
    [Фонетика]({url_phonetics})
    
    [Грамматика]({url_grammar})
    
    [Лексика]({url_lexis})
    
    [Пунктуация]({url_punctuation})
    
    [Частицы и союзы]({url_particles_and_conjunctions})
    
    [Орфография]({url_orphography})
    '''
    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)
# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.


def in_parts_of_speech():
    update.message.reply_text('да')


def in_phonetics():
    pass


def in_grammar():
    pass


def in_lexis():
    pass


def in_punctuation():
    pass


def in_particles_and_conjunctions():
    pass


def in_orphography():
    pass


def start(update, context):
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )
    print('Done!')


# def deep_linked_level_2(update, context) -> None:
#    """Reached through the SO_COOL payload"""
#    bot = context.bot
#    url = helpers.create_deep_linked_url(bot.username, 'nothing')
#    text = f"[Части речи]({url})."
#    update.message.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


def main():
    token = '1797940789:AAENadc1txh59h5FX3Kd_DMUrBECpiYwu9g'

    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.

    # Регистрируем обработчик в диспетчере.

    dp.add_handler(CommandHandler("textbook", textbook))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(CommandHandler("start", in_parts_of_speech, Filters.regex('parts-of-speech')))
    dp.add_handler(CommandHandler("start", in_phonetics, Filters.regex('phonetics')))
    dp.add_handler(CommandHandler("start", in_grammar, Filters.regex('grammar')))
    dp.add_handler(CommandHandler("start", in_lexis, Filters.regex('lexis')))
    dp.add_handler(CommandHandler("start", in_punctuation, Filters.regex('punctuation')))
    dp.add_handler(CommandHandler("start", in_particles_and_conjunctions, Filters.regex('particles-and-conjunctions')))
    dp.add_handler(CommandHandler("start", in_orphography, Filters.regex('orphography')))
    # Запускаем цикл приема и обработки сообщений.

    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
