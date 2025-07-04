import os
import telebot
from keep_alive import keep_alive

# Initialize the bot with your token
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

# Command handlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Hello! I'm a simple Telegram bot running on Replit!")

@bot.message_handler(commands=['echo'])
def echo_message(message):
    text = message.text[6:]  # Remove '/echo ' from the message
    if text:
        bot.reply_to(message, f"🔊 You said: {text}")
    else:
        bot.reply_to(message, "Please provide some text after /echo")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"🤖 You said: {message.text}")

# Start the bot
if __name__ == '__main__':
    keep_alive()  # This is for Replit to keep the bot alive
    bot.polling()
