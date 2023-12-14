import logging
from typing import Callable, Union
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import filters, MessageHandler,ApplicationBuilder, ContextTypes, CommandHandler, CallbackContext
from random import randint
import requests
from datetime import datetime
import pytz

tehran_timezone = pytz.timezone('Asia/Tehran')
current_time = datetime.now(tehran_timezone)
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
datet = formatted_time.split()
datetstr = 'امروز: ' + ' ' + str(datet[0]) + '\n' + 'ساعت: ' + ' ' + str(datet[1]) + '\n' + ' به وقت: ' + ' ' + 'GMT+3:30'


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=13cfa25ee797490893597337025a17b0')
response = requests.get(url)
data = response.json()

articles = data['articles']


words = ['list of desiered words']


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button1_row = [KeyboardButton('Music'), KeyboardButton('News')]
    button2_row = [KeyboardButton('Help')]
    keyboard = [button1_row, button2_row]

    Markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text('Choose an option:', reply_markup=Markup)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button1_row = [KeyboardButton('Music'), KeyboardButton('News')]
    button2_row = [KeyboardButton('Help')]
    keyboard = [button1_row, button2_row]

    Markup = ReplyKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome!!!')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hope To Be Helpful')
    await update.message.reply_text('Please choose an option:', reply_markup=Markup)


async def massage_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chanel_name = await context.bot.get_chat('@YOUR_CHANELL')

    message = update.message

    for i in message.text.split():
        if i in chanel:
            await context.bot.forwardMessage(chat_id=update.effective_chat.id, from_chat_id=chanel_name.id,
                                             message_id='%i'%randint('The number range of channel post IDs'))

        elif i == 'news':
            news = ''
            for i in range(len(articles)):
                news += f'{i + 1}. ' + articles[i]['title'] + ':'
                news += '\n'
                news += articles[i]['description']
                news += '\n'
            await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text=news)

        elif i == 'datetime':
            await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text= datetstr)

async def prmessage_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chanel_name = await context.bot.get_chat('@YOUR_CHANELL')

    message = update.message
    if message.text in 'Music':
        Markup = ReplyKeyboardMarkup([['The_Artist',], ['/Home']])
        await update.message.reply_text('Choose your playlist: ', reply_markup=Markup)

    elif message.text in 'Help':
        help = "🎵 To get the playlist of the artist you want press or write 'Help'." + '\n' + '\n' + "📰 To get news headlines, press or write 'News' and then choose the title to get the specifics."  + '\n' + '\n' 'Created By @Shb_80'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=help)

    elif message.text == 'words':
        for i in range('The number range of channel post IDs'):
            await context.bot.forwardMessage(chat_id=update.effective_chat.id, from_chat_id=chanel_name.id,
                                            message_id='%i' % i)
 
    elif message.text in 'News':
        ls1 = [['/home']]
        news = ''
        for i in range(len(articles)):
            news += f'{i + 1}. ' + articles[i]['title'] + ':'
            news += '\n'
            news += articles[i]['description']
            news += '\n'
            ls1.append(['title ' + str(i + 1)])
        Markup = ReplyKeyboardMarkup(ls1)
        await update.message.reply_text('Headlines of today: ', reply_markup=Markup)
        await context.bot.send_message(chat_id=update.effective_chat.id,text=news)


    elif message.text.split()[0] in 'title':
        for i in range(len(articles) + 1):
            pub = articles[i - 1]['publishedAt']
            if message.text in f'title {i}':
                news = ''
                news += 'published: ' + pub[:10]
                news += '\n'
                news += f'{i}. ' + articles[i - 1]['title'] + ':'
                news += '\n'
                news += articles[i - 1]['description']
                news += '\n'
                con = articles[i - 1]['content']
                ima = articles[i - 1]['urlToImage']
                url = articles[i - 1]['url']
                await context.bot.send_photo(chat_id=update.effective_chat.id,photo=ima)
                await context.bot.send_message(chat_id=update.effective_chat.id, text=news)
                await context.bot.send_message(chat_id=update.effective_chat.id, text=con + '\n' + 'for more: ' + '\n' + url)
                break

#
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='invalid command' + '\n' + 'Please choose an option:')
#



if __name__ == '__main__':
    application = ApplicationBuilder().token('BOTFATHER TOKEN').build()

    massage_handler = MessageHandler(filters.TEXT & filters.ChatType.GROUP, massage_response)
    start_handler = CommandHandler('start', start)
    home_handler = CommandHandler('Home', home)
    prmessage_handler = MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, prmessage_response)


    application.add_handler(massage_handler)
    application.add_handler(start_handler)
    application.add_handler(home_handler)
    application.add_handler(prmessage_handler)


    application.run_polling()
