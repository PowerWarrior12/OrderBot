#coding:utf-8
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token
from Parser import get_id_last_ad
import time
import asyncio

bot = Bot(token)
dp = Dispatcher(bot)

Sections = []
users_id = []

def start():
    f = open('Sections.txt')
    for line in f:
        Sections.append(line.strip())
    f = open('UsersId.txt')
    for line in f:
        users_id.append(line.strip())

async def write_id(id):
    f = open('UsersId.txt','a')
    f.write(str(id))
    f.close()
    users_id.append(str(id))

@dp.message_handler(commands=['start'])
async def answer_from_start(ms:types.Message):
    await bot.send_message(ms.from_user.id,'Stay away')
    
@dp.message_handler(commands=['register'])
async def register(ms:types.Message):
    await write_id(ms.from_user.id)
    await bot.send_message(ms.from_user.id,'Вы успешно подписались на рассылку')

async def check_new_ad(sec):
    while True:
        await asyncio.sleep(sec)
        url = 'https://www.fl.ru/projects/'
        id = get_id_last_ad(url,Sections)
        if id:
            f = open('id.txt','r')
            last_id = f.read()
            f.close()
            if last_id != id:
                text_message = open('text.txt','r').read()
                for us_id in users_id:
                    await bot.send_message(int(us_id),text_message)
                with open('id.txt','w') as f:
                    f.write(id)



if __name__ == '__main__':
    start()
    dp.loop.create_task(check_new_ad(10))
    executor.start_polling(dp,skip_updates=True)