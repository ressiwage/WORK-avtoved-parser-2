import json, requests, datetime, asyncio
from config import Config
from auth import auth
from utils import download_image, send_tg_message, sync_db


def post(item):
    r = requests.post('https://api.vk.com/method/wall.post', data=item)
    if r.json().get('response') is not None and r.json()['response']['post_id'] is not None:
        return True
    else:
        raise Exception(f'Error while posting: {r.text}')
    
def main(threshold=3600):
    '''if amount_of_posts = -1 then publish all the posts;
    threshold is in seconds'''
    try:
        database = json.load(open('db.json', 'r', encoding='utf8'))
    except FileNotFoundError as e:
        raise e
    ses=auth()
    posted_tg = set(database.get('posted_tg', []))
    database['last_tg_post'] = database.get('last_tg_post', 0)
    for item in database['items']:
        if item in posted_tg:
            continue

        if 0 and not datetime.datetime.now().timestamp() - database['last_tg_post']>=threshold:
            continue

        wall_item = {
            'message': database['items'][item]['title'] + '\n\n' + database['items'][item]['text'] + '\n\n' + database['items'][item]['post_url'],
        }
        img = None
        if database['items'][item].get('image') is not None:
            download_image(database['items'][item]['image'], ses)
            img = 'temp_image.jpg'

        asyncio.run(send_tg_message(Config.BOT_TOKEN, Config.CHAT_ID, img, wall_item['message']))
        database['posted_tg'] = database.get('posted_tg', []) + [item]
        database['last_tg_post'] = datetime.datetime.now().timestamp()
        database = sync_db(database)
        break
    return True
