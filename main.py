import asyncio
from aiogram import Bot, Dispatcher, types
from config.config import TOKEN
from database import database as db
from handler.handler import router


async def on_startup(_):
    try:
        await db.create_database()

    except Exception as e:
        print(f"Ошибка при старте базы данных: {e}")
    finally:
        print('Бот успешно запущен')

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await dp.start_polling(bot, on_startup=on_startup)
    except KeyboardInterrupt:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("STOPPED")