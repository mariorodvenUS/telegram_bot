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

"Bloque de texto comentado, es una funcion que toma cualquier mensaje y menciona a quien lo haya enviado"
# Manejador de mensajes que no son comandos
@bot.message_handler(func=lambda message: True)

def scan_message(message): # función que se ejecuta cada vez que se envía un mensaje.
    palabras = message.text.split() #Divide el texto del mensaje en todas las palabras que lo componen y lo guarda en palabras.
    numeros={"1":"Chupa como si fuese zumo ;P", "uno":"Chupa como si fuese zumo ;P",
             "2":"Por la garganta hasta que te entre tos ;P","dos":"Por la garganta hasta que te entre tos ;P", 
             "3":"Te la meto del revés", "tres":"Te la meto del revés",
             "4":"Agárramela un rato ;P", "cuatro":"Agárramela un rato ;P",
             "5":"Por el culo te la hinco (REORIGINAL pibe) ;P", "inco":"Por el culo te la hinco (REORIGINAL pibe) ;P",
             "6":"A ver si la meteis ;P", "seis":"A ver si la meteis ;P",
             "7":"Por el culo te la mete ;P", "siete":"Por el culo te la mete ;P",
             "8":"Por el culo te la entrocho ;P", "ocho":"Por el culo te la entrocho ;P", 
             "9":"Agárramela que se mueve ;P", "nueve":"Agárramela que se mueve ;P",
             "0":"No haré rima pues soy un caballero", "cero":"No haré rima pues soy un caballero"}
    terminaciones = {"ado":"el que tengo aquí colgado ;P", "eto":"Tú te agachas y yo te la meto ;P",
                     "ones":"pues agárrame los cojones :P", "ojos":"El que te metió la polla y te nubló los ojos ;P",
                     "obra": "pues chúpamela que tengo de sobra ;P", "uca":"El de los huevos con peluca ;P",
                     "ena":"El de mi polla rellena ;P", "otas":"un picor en las pelotas ;P", 
                     "ulo":"El que te dio por el culo ;P", "itos": "el de los cojones pequeñitos",
                     "rojo":"Tiempo de hambre y piojo'"
                     }
    secuencias={**numeros, **terminaciones}
    for palabra in palabras:
        for secuencia,rima in secuencias:
            if palabra.endswith(secuencia):
                bot.reply_to(message, rima)


   

            """def echo_all(message):
    username = message.from_user.username if message.from_user.username else "Usuario desconocido"
    bot.reply_to(message, f"¡Hola, @{username}! Soy un bot de prueba. ¡Gracias por iniciar la conversación!")
            """


# Iniciar el bot
bot.polling()