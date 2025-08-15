from auth import auth
from config import Config 
import json, hashlib, datetime
def main(pages_amount=1):
    from bs4 import BeautifulSoup, element
    from config import PathTo
    ses = auth()

    try:
        database = json.load(open('db.json', 'r', encoding='utf8'))
    except FileNotFoundError:
        json.dump({'items':{}, 'posted':[], 'last_post':datetime.datetime.now().timestamp()}, open('db.json', 'w+', encoding='utf8'), ensure_ascii=False, indent=2)
        database = json.load(open('db.json', 'r', encoding='utf8'))
    for ITERATION in range(pages_amount):
        if ITERATION==0:
            url = Config.base_url
        else:
            url=f"{Config.base_url}?page="+str(ITERATION+1)
        #auth()
        page = ses.get(url)
        mainpage_soup = BeautifulSoup(page.content, 'html.parser')
        containers = mainpage_soup.select(PathTo.container)
        items = database['items']

        ##containers.items_append

        for container in containers:
            if (post_link:=container.select_one(PathTo.post_link)) is not  None:
                post_url = Config.base_url+post_link['href']
                title = ''
                for child in post_link:
                    if isinstance(child, element.NavigableString):
                        title = child.get_text().strip()
            if (container_text:=container.select_one(PathTo.text_in_container)) is not None:
                content = container_text
            text = content.get_text()
            while '\t' in text:
                text=text.replace('\t', '')
            while '\n' in text:
                text = text.replace('\n', ' ')
            while '  ' in text:
                text = text.replace('  ', ' ')
            image = None
            for a in content.select('a'):
                if (img:=a.select_one('img')) is not None and img.get('src') is not None:
                    # image = Config.base_url+img['src']
                    image = a['href']
                    # image_soup = BeautifulSoup(ses.get(a['href']).content, 'html.parser')
                    # # print(ses.get(a['href']).text)
                    # if (img_highres:=image_soup.select_one(PathTo.highres_image)) is not None:
                    #     print(img_highres.text)
                    #     image = img_highres.text
            hash_title = str(hashlib.md5(bytes(title, "utf-8")).hexdigest())
            items[hash_title] = {
                'title':title,
                'text':text,
                'post_url':post_url,
                'image':image
            }
    json.dump(database, open('db.json', 'w+', encoding='utf8'), ensure_ascii=False, indent=2)
    return True
            
if __name__=='__main__':    
    main()
