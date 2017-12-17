import telebot

TOKEN = '507137151:AAFGTnLPTJEqZzmlYZhbA0Tm_9pnOGmy_zg' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Привет, как к тебе обращаться??')
    bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, '{name}, значит. Рад тебя видеть!'.format(name=message.text))

bot.polling()    
