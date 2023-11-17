import telebot
from dotenv import load_dotenv
import random
import os

from cosas_llave import llave

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)
print("bot creado")
# Manejador del comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("empezao")
    bot.reply_to(message, "¡Hola! Soy un bot de prueba. ¡Gracias por iniciar la conversación!")

#codigo para la llave
# esto se puede optimizar en memoria pero no lo hago para mantener la legibilidad
@bot.message_handler(commands=['llave'])
def coger_llave(message):
    username = message.from_user.username if message.from_user.username else "Usuario_desconocido"
    hora_mensaje = llave.coger(username)
    bot.reply_to(message, f"@{username} ha cogido la llave a las {hora_mensaje}")
   
@bot.message_handler(commands=['where_llave'])
def consultar_llave(message):
    llavero = llave.consultar()
    if llavero == -1:
        bot.reply_to(message, "Ha pasado algo, y es que el archivo no existe, escribe el comando //llave o //llavent para crearlo")
    else:
        bot.reply_to(message, f"La llave la tiene @{llavero}")

@bot.message_handler(commands=['llavent'])  
def dejar_llave(message):
    username = message.from_user.username if message.from_user.username else "Usuario_desconocido"
    hora_mensaje = llave.dejar()
    bot.reply_to(message, f"@{username} ha dejado la llave en copisteria a las {hora_mensaje}")

# Iniciar el bot
bot.polling()

