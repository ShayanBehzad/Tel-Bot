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


# 13cfa25ee797490893597337025a17b0

# wfIfK5cZPyszntAehKZsGGxO9DifSNCeur/u0+pZpzFV/NPE

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# shoh apikey: 4ab98c293d4d4146ab4b89a5a9243842
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=13cfa25ee797490893597337025a17b0')
response = requests.get(url)
data = response.json()

articles = data['articles']

#
# love_list = ['daryamoradii', 'moauraa', 'sepehrmnp', 'aryanmnp', 'shayanbenzad']
# gls = ['شایان','شاشان','بهزاد','شاشا']
poori = ['پوری','کفتر','سیبیل','گاد','غیرت','زانتیا']
doki = ['هیپهاپولوژیست','دکی','دکتر','مازندران','لندنی','وحشی','عمل']


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button1_row = [KeyboardButton('Music'), KeyboardButton('News')]
    button2_row = [KeyboardButton('Help')]
    keyboard = [button1_row, button2_row]

    Markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text('Choose an option:', reply_markup=Markup)
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button1_row = [KeyboardButton('Music'), KeyboardButton('News')]
    button2_row = [KeyboardButton('Help')]
    keyboard = [button1_row, button2_row]

    Markup = ReplyKeyboardMarkup(keyboard)

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome!!!')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hope To Be Helpful')
    await update.message.reply_text('Please choose an option:', reply_markup=Markup)


async def massage_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chanel_poori = await context.bot.get_chat('@poooorii')
    chanel_doki = await context.bot.get_chat('@hipdok')

    message = update.message
    # user_id = update.message.from_user
    # await context.bot.send_message(chat_id=chanel_poori.id,text=str(message.id) + '  ' + 'salam')

    # if message.text in 'ریی':
    #     await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text='فکش رییییی')
    #
    # elif message.text in 'ربات' :
    #     if str(user_id['id']) in '86756573':
    #         await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id,text='سلطانی آقا شایان')
    #     elif str(user_id['username']) in love_list:
    #         await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id,text='جون دلم')
    #
    #     else:
    #         await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id,text='کیر')
    #

    # elif str(user_id['id']) in '5894900425':
    #     await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text='آخه چقد تو دولی آرش')

    for i in message.text.split():
        # if i in gls:
        #     if str(user_id['username']) in love_list:
        #         await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text=f'عای {i} فدات شه')
        #         break
        #     else:
        #         await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text='کیر')
        #         break
        # elif i in 'سینا':
        #     await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text='سینا پیپیه')
        #     break



        if i in poori:
            await context.bot.forwardMessage(chat_id=update.effective_chat.id, from_chat_id=chanel_poori.id,
                                             message_id='%i'%randint(2,11))
        elif i in doki:
            await context.bot.forwardMessage(chat_id=update.effective_chat.id, from_chat_id=chanel_doki.id,
                                            message_id='%i' % randint(3, 13))

        elif i == 'اخبار':
            news = ''
            for i in range(len(articles)):
                news += f'{i + 1}. ' + articles[i]['title'] + ':'
                news += '\n'
                news += articles[i]['description']
                news += '\n'
            await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text=news)

        elif i == 'تاریخ':
            await context.bot.send_message(chat_id=update.effective_chat.id, reply_to_message_id=update.effective_message.id, text= datetstr)

async def prmessage_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chanel_poori = await context.bot.get_chat('@poooorii')
    chanel_doki = await context.bot.get_chat('@hipdok')

    message = update.message
    if message.text in 'Music':
        Markup = ReplyKeyboardMarkup([['Hiphopologist', 'Poori'], ['/Home']])
        await update.message.reply_text('Choose your playlist: ', reply_markup=Markup)

    elif message.text in 'Help':
        help = "🎵 To get the playlist of the artist you want press or write 'Help'." + '\n' + '\n' + "📰 To get news headlines, press or write 'News' and then choose the title to get the specifics."  + '\n' + '\n' 'Created By @Shb_80'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=help)

    elif message.text == 'Hiphopologist':
        for i in range(3,14):
            await context.bot.forwardMessage(chat_id=update.effective_chat.id, from_chat_id=chanel_doki.id,
                                            message_id='%i' % i)
    elif message.text == 'Poori':
        for i in range(2, 12):
            await context.bot.forwardMessage(chat_id=update.effective_chat.id, from_chat_id=chanel_poori.id,
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
    application = ApplicationBuilder().token('6660229378:AAERnzDGQMTzS3ufhokQpwgDG3PoN_p-fj4').build()

    massage_handler = MessageHandler(filters.TEXT & filters.ChatType.GROUP, massage_response)
    start_handler = CommandHandler('start', start)
    home_handler = CommandHandler('Home', home)
    prmessage_handler = MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, prmessage_response)


    application.add_handler(massage_handler)
    application.add_handler(start_handler)
    application.add_handler(home_handler)
    application.add_handler(prmessage_handler)


    application.run_polling()