import sqlite3
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
router = Router()

def create_database():
    conn = sqlite3.connect('crossovers.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS categories ( category_id INTEGER PRIMARY KEY AUTOINCREMENT, category_name TEXT NOT NULL ); ''')
    cursor.execute(''' CREATE TABLE IF NOT EXISTS shoes ( shoe_id INTEGER PRIMARY KEY AUTOINCREMENT, model_name TEXT NOT NULL, brand TEXT, price INTEGER, image_url TEXT, category_id INTEGER, FOREIGN KEY (category_id) REFERENCES categories(category_id) ); ''')
    #cursor.execute('''CREATE TABLE IF NOT EXISTS shoes (id INTEGER PRIMARY KEY AUTOINCREMENT, model_name TEXT NOT NULL, brand TEXT, price INTEGER, image_url TEXT, category TEXT)''')

    conn.commit()
    conn.close()

def insert_categories(categories):
    conn = sqlite3.connect('crossovers.db')
    cursor = conn.cursor()
    for category in categories:
        cursor.execute(''' INSERT INTO categories (category_name) VALUES (?); ''',
                       (category, ))

    conn.commit()
    conn.close()

def insert_shoes(shoes):
    conn = sqlite3.connect('crossovers.db')
    cursor = conn.cursor()

    for shoe in shoes:
        cursor.execute(''' INSERT INTO shoes (model_name, brand, price, image_url, category_id) VALUES (?, ?, ?, ?, ?); ''', (shoe[0], shoe[1], shoe[2], shoe[3], shoe[4]))

    conn.commit()
    conn.close()
dbcategories = ['Спортивные', 'Повседневные', 'Детские']
#create_database()
#insert_categories(dbcategories)

shoes = [
    ('Nike Air Max 270', 'Nike', 400, 'https://sneakers.by/image/cache/catalog/sneakers-pics/101151/krossovki-nike-wmns-max-270-ah6789-100-4-800x800.jpg', 1),
    ('Adidas Superstar', 'Adidas', 250, 'https://sneakers.by/image/cache/catalog/sneakers-pics/32998/kedy-adidas-superstar-j-ef5398-1-695x695.jpg', 2),
    ('Reebok Classic Leather', 'Reebok', 250, 'https://sneakers.by/image/cache/catalog/sneakers-pics/29502/krossovki-reebok-classic-leather-gy0952-2-800x800.jpg', 2),
    ('Puma Suede Classic+', 'Puma', 250, 'https://sneakers.by/image/cache/catalog/sneakers-pics/105889/kedy-puma-suede-classic-399781-01-1-800x800.jpg', 2),
    ('Converse Chuck Taylor All Star', 'Converse', 300, 'https://converseshoes.by/wp-content/uploads/2023/12/kedy-converse-chuck-70-chernye-vysokie-162050s-kupit-v-minske-original-chernye-konversy-minsk.jpg', 3)
]
#insert_shoes(shoes)


async def get_items_by_category(category_index):
    conn = sqlite3.connect('crossovers.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT shoe_id, model_name, brand, price, image_url FROM shoes WHERE category_id = ? ''', {"index": category_index})
    items = cursor.fetchall()
    conn.close()
    return items


@router.callback_query(lambda c: c.data.startswith('category_'))
async def process_category_callback(callback_query: CallbackQuery):
    category_index = int(callback_query.data.split('_')[1])
    category = categories[category_index]
    items = await get_items_by_category(category_index)
    text = ""
    if items:
        for item in items:
            text += f"\n• {item['model_name']} - {item['brand']} - {item['price']}"
        await callback_query.message.answer(text)
    else:
        await callback_query.message.answer(f"В категории '{category}' нет товаров.")
