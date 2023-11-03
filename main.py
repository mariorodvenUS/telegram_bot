import telebot
from dotenv import load_dotenv
import random
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)

# Manejador del comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy un bot de prueba. ¡Gracias por iniciar la conversación!")

"""Bloque de texto comentado, es una funcion que toma cualquier mensaje y menciona a quien lo haya enviado
# Manejador de mensajes que no son comandos
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    username = message.from_user.username if message.from_user.username else "Usuario desconocido"
    bot.reply_to(message, f"¡Hola, @{username}! Soy un bot de prueba. ¡Gracias por iniciar la conversación!")
"""
# Iniciar el bot
bot.polling()