import telebot 
import config
from extensions import APIException, CurrencyConverter
#импортируем библиотеку pyTelegramBotAPI, далее импортируем файл с токеном
#классы из файла extensions
bot = telebot.TeleBot(config.TOKEN)#создаем обьект Telebot и передем ему 
                                   #токен нашего бота

#Эта функция обрабатывает команды /start и /help. 
#Oна отправляет пользователю сообщение с инструкциями по использованию бота.
@bot.message_handler(commands=["start", "help"])
def handle_start_help(message: telebot.types.Message):
    text = (
        "Привет! Я бот, который может вернуть цену на определенное количество валюты.\n"
        "Для этого отправь мне сообщение в формате: \n"
        "<имя валюты, цену которой ты хочешь узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.\n"
        "Например: USD RUB 100\n"
        "Чтобы узнать список всех доступных валют, используй команду /values."
    )
    bot.reply_to(message, text)

#Эта функция обрабатывает команду /values. 
#Она отправляет пользователю сообщение со списком доступных валют.
@bot.message_handler(commands=["values"])
def handle_values(message: telebot.types.Message):
    text = (
        "Доступные валюты:\n"
        "USD - Доллар США\n"
        "EUR - Евро\n"
        "RUB - Российский рубль\n"
    )
    bot.reply_to(message, text)
#Эта функция обрабатывает текстовые сообщения
@bot.message_handler(content_types=["text"])
def handle_text(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise APIException("Неверный формат запроса. Используйте команду /help для получения инструкций.")
        
        base, quote, amount = values
        amount = float(amount)
        #Она получает текст сообщения, разбивает его на три части 
        #(имя первой валюты, имя второй валюты и количество первой валюты)
        result = CurrencyConverter.get_price(base.upper(), quote.upper(), amount)
        text = f"Стоимость {amount} {base.upper()} в {quote.upper()} = {result:.2f} {quote.upper()}"
    except APIException as e:
        text = f"Ошибка: {e}"
    except ValueError:
        text = "Неверный формат числа."
    except Exception:
        text = "Произошла ошибка."

    bot.reply_to(message, text)

#запускаем нашего бота в бесконечном цикле 
bot.polling(none_stop=True)    