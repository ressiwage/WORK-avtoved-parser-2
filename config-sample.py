class PathTo:
    # CSS селектор для контейнеров с новостями на главной странице
    container = 'ol.ctaFtListItemsPage>li.ctaFtBlockPage'
    # css селектор для ссылки на пост в контейнере
    post_link = '.sectionMain .ctaFtThreadTitlePage a'
    # ненужное
    text_in_post = '.messageContent article blockquote'
    # ненужное
    title_in_container = 'h3.ctaFtThreadTitlePage'
    # css селектор текст в контейнере на главной странице
    text_in_container = 'div.baseHtml'
    # ненужное
    highres_image='body>img'

class Config:
    username='' #логин 
    password=''#пароль 
    amount_of_pages = 1 # сколько страниц парсить
    amount_of_posts = 10 # сколько постов постить за итерацию, -1 значит все что имеются
    interval_seconds = 1800 # через какой интервал запускать бота
    tg_threshold = 1800 #интервал между постами в боте

    #то что ниже не менять!
    base_url = 'some-domen-on-xenforo'
    group_id = 000
    album_id = 000
    version = ''
    at = ''
    protected_key = ''
    service_key = ''
    CHAT_ID = ''      # ид чата канала
    BOT_TOKEN = ''  # токен тг бота

