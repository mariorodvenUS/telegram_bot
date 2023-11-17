import telebot
from dotenv import load_dotenv
import random
import os
import requests,json,time
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)
# Manejador del comando /start
@bot.message_handler(commands=['weather'])
def send_question(message):
    bot.reply_to(message, "Hi! I'm here to help you, please tell me the name of the city or town")
    bot.register_next_step_handler(message, get_city)




def get_city(message):
    chat_id = message.chat.id
    city = message.text
    bot.send_message(chat_id, f"The temperature of {city.capitalize()} today is {get_weather(city)[0]}ºC and the weather is {get_weather(city)[1]} ")
    #time.delay(0.5)
    #bot.send_message(chat_id, f"On the other hand, if you're interested in tomorrow's weather forecast, you should know that the temperature of {city.capitalize()} for tomorrow will be {get_weather(city)[2]}ºC and the weather will be {get_weather(city)[3]} ")
    
    
    
    
def get_weather(city):
    
    #THE WEATHER FOR TODAY
    urlToday = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid=964de7ef9e3148a1ce7d08875382dcae&units=metric".format(city)
    responseToday = requests.get(urlToday)
    dataToday = responseToday.json()
    
    tempToday = dataToday['list'][0]['main']['temp']
    weatherToday = dataToday['list'][0]['weather'][0]['main']
    
    #THE WEATHER FOR TOMORROW
    """urlTomorrow = "https://pro.openweathermap.org/data/2.5/forecast/hourly?q={}&appid=964de7ef9e3148a1ce7d08875382dcae&units=metric".format(city)
    responseTomorrow = requests.get(urlTomorrow)
    dataTomorrow = responseTomorrow.json()
    print(dataTomorrow)
    tempTomorrow = dataTomorrow['list'][0]['main']['temp']
    weatherTomorrow = dataTomorrow['list'][0]['weather'][0]['main']"""
    
    
    
    
    return tempToday,weatherToday
        

def send_weather(message):
    chat_id = message.chat.id
    city = get_city(message)
    temp, wind_speed, latitude, longitude, description = get_weather(city)
    bot.reply_to(message, f"Temperatura = {temp}")
    bot.reply_to(message, f"Velocidad del viento = {wind_speed}")
    bot.reply_to(message, f"Latitud = {latitude}")
    bot.reply_to(message, f"Longitud = {longitude}")
    bot.reply_to(message, f"Descripción = {description}")

#bot.send_message(chat_id, get_weather(message))
"""Bloque de texto comentado, es una funcion que toma cualquier mensaje y menciona a quien lo haya enviado
# Manejador de mensajes que no son comandos
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    username = message.from_user.username if message.from_user.username else "Usuario desconocido"
    bot.reply_to(message, f"¡Hola, @{username}! Soy un bot de prueba. ¡Gracias por iniciar la conversación!")
"""
# Iniciar el bot
bot.polling()


