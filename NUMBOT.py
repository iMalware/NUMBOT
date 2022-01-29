import telebot
import json
from urllib.request import urlopen
import re
token = (input('Your token'))
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def  message(message):
    bot.send_message(message.chat.id,f"Start message",parse_mode="markdown",disable_web_page_preview="true")
@bot.message_handler(func=lambda message: True)
def muh(message):
  try:
      msg = message.text
      if "05" in msg and len(msg) == 10 and not re.findall('[a-zA-Z+ا-ي٠-٩]+', msg):
        r = urlopen(f"https://tyfytfytfyt.000webhostapp.com/server.php?number={msg}")
        res = [sub['Name'] for sub in json.loads(r.read())]
        text = "\n"
        for i in res:
          text +=f"- {i}\n"
        bot.send_message(message.chat.id,f'{text}\n\n',parse_mode='markdown',disable_web_page_preview=True)
      else:
        bot.send_message(chat_id=message.chat.id,text='*الرقم غير صحيح*',parse_mode='markdown')
  except:
    bot.send_message(chat_id=message.chat.id,text='*الرقم غير مسجل*',parse_mode='markdown')
bot.polling(True)

##by MUH , TW:not1me
