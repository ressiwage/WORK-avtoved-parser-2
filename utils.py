import os, json
from telegram import Bot, InputFile
from datetime import datetime, timedelta
import asyncio


def download_image(url, ses):
    img_data = ses.get(url).content
    name = f'temp_image.jpg'
    with open(name, 'wb+') as handler:
        handler.write(img_data)
    return name


async def send_tg_message(BOT_TOKEN, CHAT_ID, IMAGE_PATH, MESSAGE_TEXT, ):
    bot = Bot(token=BOT_TOKEN)
    
    # Проверяем существование файла изображения
    if IMAGE_PATH is not None and not os.path.exists(IMAGE_PATH):
        raise Exception(f"Ошибка: файл {IMAGE_PATH} не найден!")
    
    if IMAGE_PATH is not None:
        # Открываем файл изображения
        with open(IMAGE_PATH, 'rb') as photo_file:
            # Отправляем отложенное сообщение
            return await bot.send_photo(
                chat_id=CHAT_ID,
                photo=InputFile(photo_file),
                caption=MESSAGE_TEXT,
            )
    else:
        return await bot.send_message(
                chat_id=CHAT_ID,
                text=MESSAGE_TEXT,
            )
    
def sync_db(database):
    json.dump(database, open('db.json', 'w+', encoding='utf8'), ensure_ascii=False, indent=2)
    return json.load(open('db.json', 'r', encoding='utf8'))