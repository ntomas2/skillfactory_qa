import telebot
from extensions import APIException, CurrencyConverter
from config import currency_dict, API_TOKEN


bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = '''
    Чтобы начать работу введите команду боту в следующем формате:
    \n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>
    \nУвидеть список доступных валют: /values
    '''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    currency = 'Доступные валюты:\n' + '\n'.join(currency_dict.keys())
    bot.send_message(message.chat.id, currency)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        if len(message.text.split()) != 3:
            raise APIException('Неверное количество параметров')
        quote, base, amount = message.text.split()
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
