import json, requests, datetime
from config import Config
from auth import auth
from vkuploader import upload_image

def post(item):
    r = requests.post('https://api.vk.com/method/wall.post', data=item)
    if r.json().get('response') is not None and r.json()['response']['post_id'] is not None:
        return True
    else:
        raise Exception(f'Error while posting: {r.text}')
def main(amount_of_posts=10, threshold=3600):
    '''if amount_of_posts = -1 then publish all the posts;
    threshold is in seconds'''
    try:
        database = json.load(open('db.json', 'r', encoding='utf8'))
    except FileNotFoundError as e:
        raise e
    ses=auth()
    posted = set(database.get('posted', []))
    c = amount_of_posts
    for item in database['items']:
        if item in posted:
            continue
        
        if c<0:
            continue
        
        if database['last_post']<datetime.datetime.now().timestamp():
            database['last_post'] = datetime.datetime.now().timestamp()
        p_date = int(database['last_post']) + threshold 
        wall_item = {
            'owner_id':f'-{Config.group_id}',
            'message': database['items'][item]['title'] + '\n\n' + database['items'][item]['text'] + '\n\n' + database['items'][item]['post_url'],
            'from_group':1,
            'signed':0,
            'v':Config.version,
            'access_token': Config.at,
            'publish_date': str(
                p_date
            ),
        }
        if database['items'][item].get('image') is not None:
            image_id = upload_image(database['items'][item]['image'], ses)
            wall_item['attachments'] = f'photo-{Config.group_id}_{image_id}'
        if post(wall_item):
            c-=1
            database['last_post'] = p_date
            database['posted'].append(item)
            json.dump(database, open('db.json', 'w+', encoding='utf8'), ensure_ascii=False, indent=2)
            database = json.load(open('db.json', 'r', encoding='utf8'))
    return True
