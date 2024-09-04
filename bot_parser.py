import asyncio
import time
import json
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from cian_parser import main, url
from aiogram.filters import Command
import asyncio
from aiohttp import ClientSession

TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher()
Flag = True

@dp.message(Command("stop"))
async def stop(message: Message):
    global Flag
    Flag = False
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Бот остановлен, используйте /start для его включения')

@dp.message(Command("start"))
async def cian_parsing(message: Message):
    global Flag
    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text='Бот включен, используйте /stop для его выключения')
    main()
    with open('result_cian.json', encoding = "UTF-8") as file:
        result = json.load(file)
        
    await bot.send_message(chat_id=user_id, text="Текущие актуальные обьявления:")
    for i in range (3):
        await bot.send_message(chat_id=user_id, text=str(result[i].get('price') +"\n\n"+ result[i].get('url')))

    while Flag:
        time.sleep(900)
        result_temp = result[0]
        main()

        if result_temp != result[0]:
            bot.send_message(chat_id=user_id, text='Появилось новое обьявление:')
            bot.send_message(chat_id=user_id, text=str(result[0].get('price') +"\n\n"+ result[0].get('url')))
            


async def bot_main():
    await dp.start_polling(bot)
    async with ClientSession(trust_env=True) as session:
        async with session.get(url) as resp:
            print(resp.status)


if __name__ == "__main__":
    try:
        asyncio.run(bot_main())
    except KeyboardInterrupt:
        print("Бот выключен")