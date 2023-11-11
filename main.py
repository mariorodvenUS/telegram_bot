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
   
@bot.message_handler(commands=['llave?'])
def consultar_llave(message):
    llavero = llave.consultar()
    bot.reply_to(message, f"La llave la tiene @{llavero}")

@bot.message_handler(commands=['llavent'])  
def dejar_llave(message):
    username = message.from_user.username if message.from_user.username else "Usuario_desconocido"
    hora_mensaje = llave.dejar()
    bot.reply_to(message, f"@{username} ha dejado la llave en conserjeria a las {hora_mensaje}")




"""
@bot.message_handler(commands=['tatequieto'])
def tatequieto(message):
    bot.reply_to(message, "perdon ya me apago")
    bot.stop_polling()
    print("apagao")
    
Bloque de texto comentado, es una funcion que toma cualquier mensaje y menciona a quien lo haya enviado
# Manejador de mensajes que no son comandos
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    username = message.from_user.username if message.from_user.username else "Usuario desconocido"
    bot.reply_to(message, f"¡Hola, @{username}! Soy un bot de prueba. ¡Gracias por iniciar la conversación!")
"""



# Iniciar el bot
bot.polling()

