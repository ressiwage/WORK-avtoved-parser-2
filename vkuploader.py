import requests
from config import Config
import os

def _rmifexists(file):
    if os.path.exists(file):
        os.remove(file)   
    else:
        pass

def upload_image(url, ses):
    img_data = ses.get(url).content
    name = f'temp_image.jpg'
    with open(name, 'wb') as handler:
        handler.write(img_data)


    r = requests.post('https://api.vk.com/method/photos.getUploadServer', data={
        'access_token':Config.at,
        'album_id':Config.album_id,
        'v':Config.version,
        'group_id':Config.group_id
    })
    # print(r.json()['response']['upload_url'])
    with open(name, 'rb') as f:
        r = requests.post(r.json()['response']['upload_url'], headers={'cache-control': "no-cache",}, files={'file1':f})
    plist = r.json()['photos_list']
    serv = r.json()['server']
    h = r.json()['hash']

    r = requests.post('https://api.vk.com/method/photos.save', data={
        'access_token':Config.at,
        'album_id':Config.album_id,
        'server':serv,
        'photos_list':plist,
        'v':Config.version,
        'hash':h,
        'group_id':Config.group_id
    })
    _rmifexists(name)
    return r.json()['response'][0]['id']

