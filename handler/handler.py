from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import keyboard as kb
import sqlite3
import database as db
router = Router()

hello = 'Приветствуем вас в нашем магазине кроссовок! 👟✨\n Мы рады видеть вас здесь! У нас вы найдете широкий ассортимент стильных и удобных кроссовок для любого повода. Если у вас есть вопросы или вы ищете что-то конкретное, не стесняйтесь обращаться к нам. Мы всегда готовы помочь! Следите за нашими новинками и акциями, чтобы не пропустить лучшие предложения. Спасибо, что выбрали нас! '

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(hello, reply_markup=kb.main_menu)

@router.callback_query(F.data == 'catalog')
async def process_catalog(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer("Выберите категорию: ", reply_markup=kb.category_keyboard_inline)

@router.callback_query(F.data.startswith("category_"))
async def category(callback_query: CallbackQuery):
    await callback_query.message.delete()
    print(await db.get_items_by_category(kb.categories[callback_query.data]))
    await callback_query.message.answer(callback_query.data.split("_")[1])


@router.callback_query(F.data == 'main_menu')
async def process_main_menu(callback_query: CallbackQuery):
    await callback_query.message.answer("Добро пожаловать в главное меню! Выберите опцию:", reply_markup=kb.main_menu)
