import telebot
from redditDownloader import download
import os

video_link = None

bot = telebot.TeleBot(
    token='6162340362:AAF49pkDUl7GN7SzvMN8rLbRSVam35bt0kw'
)


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(
        message.chat.id, 'Please send your link,and stand by.')



@bot.message_handler(func=lambda message: True)   
def get_message(message):
    chat_id = message.chat.id
    text = message.text
    video_path = download(text)
    # print(f"path:{video_path}")
    bot.send_video(chat_id=chat_id, video=open(video_path, 'rb'))
    os.remove(video_path)
    # print(f"{chat_id}: {text}")

bot.infinity_polling()
