import telebot
from main import gen_pass
from smalik import gen_small
token = ""    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)    

@bot.message_handler(commands=['kakdela'])
def send_dela(message):
    bot.reply_to(message, "[хорошо, а твои?]")

@bot.message_handler(commands=['pass'])
def send_pass(message):
    bot.reply_to(message, f"Boт ваш пароль: {gen_pass(10)}")

@bot.message_handler(commands=['smaliki'])
def send_small(message):
    bot.reply_to(message, f"Boт ваш : {gen_small(10)}")

@bot.message_handler(commands=['stop'])
def send_stop(message):
    bot.send_message(message.chat.id, "бот выключен")
    bot.stop_bot()

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("bot start")
bot.polling()
