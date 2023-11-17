import telebot
from dotenv import load_dotenv
import random
import os

import requests,json

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

def get_weather(city):
    #THE WEATHER FOR TODAY
    urlToday = "http://api.openweathermap.org/data/2.5/forecast?q={}&appid=964de7ef9e3148a1ce7d08875382dcae&units=metric".format(city)
    responseToday = requests.get(urlToday)
    dataToday = responseToday.json()
    
    tempToday = dataToday['list'][0]['main']['temp']
    weatherToday = dataToday['list'][0]['weather'][0]['main']

    return tempToday,weatherToday
        

# Iniciar el bot
bot.polling()


