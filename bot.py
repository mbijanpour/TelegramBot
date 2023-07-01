"""
    This Python code sets up a Telegram bot that can download videos from Reddit and send them to users.
    email: mahanbjanpour@gmail.com
    github: https://github.com/mbijanpour/TelegramBot
"""

import telebot
from redditDownloader import download
import os


# It initializes the Telegram bot with the provided token, which is a unique identifier for the bot.
# This token is necessary for the bot to authenticate and interact with the Telegram API.
bot = telebot.TeleBot(
    token='6162340362:AAF49pkDUl7GN7SzvMN8rLbRSVam35bt0kw'
)

# this function handel the start command in the bot


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(
        message.chat.id, 'Please send your link,and stand by.')

# this function handel the given link and pass it to the redditDownloader.py to get the video


@bot.message_handler(func=lambda message: True)
def get_message(message):

    chat_id = message.chat.id
    text = message.text
    video_path = download(text)

    if video_path == 'invalid':
        # if links was invalid, it will send a message to the user
        bot.send_message(
            message.chat.id, 'invalid link, please provide a valid reddit video link!')
    else:

        bot.send_video(chat_id=chat_id, video=open(video_path, 'rb'))
        # for deleting the video after saving it for the user (optional)
        os.remove(video_path)


# starting the bot ...
bot.infinity_polling()
