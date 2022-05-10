import os
import telebot
from dotenv import load_dotenv
from stock_api import get_stock_price

load_dotenv()
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
RAPID_API_TOKEN = os.environ.get("RAPID_API_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Olá, eu sou um bot que mostra os preços das ações listadas na Nasdaq.

Envie uma mensagem no formato "/preco NOME_DA_ACAO" para receber a resposta.
Exemplo: /preco tsla

Obs: O bot está em um servidor gratuito, de baixa performance, então tenha paciência com a demora.
""")

@bot.message_handler(commands=["preco", "preço"])
def send_price(message):
    stock_name = message.text.split()[-1]
    response = get_stock_price(stock_name, RAPID_API_TOKEN)
    bot.reply_to(message, response)

bot.infinity_polling()