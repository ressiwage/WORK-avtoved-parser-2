import requests
from config import Config

headers = {'user-Agent': 'Mozilla/5.0'}
getUrl = Config.base_url+'login/'
postUrl = getUrl + 'login'
data = {'login':Config.username,'password':Config.password, 'register':0,  'cookie_check': 1}

def auth():
    '''возвращается requests.session'''
    ses = requests.session()
    ses.get(getUrl,headers=headers)
    response = ses.post(postUrl,headers=headers,data=data)
    if 'LogOut' in response.text:
        return ses
    else:
        raise Exception(response.status_code, response.text)
