import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['name'])
def get_name(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты не создал покемона")
    else:
        bot.reply_to(message, Pokemon.pokemons[message.from_user.username].name)

@bot.message_handler(commands=['picture'])
def get_pic(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "Ты не создал покемона")
    else:
        bot.send_photo(message.chat.id, Pokemon.pokemons[message.from_user.username].show_img())


bot.infinity_polling(none_stop=True)

