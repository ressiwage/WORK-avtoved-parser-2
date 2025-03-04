from poster_annonces import main as post_main
from parser_annonces import main as parse_main
from config import Config
import traceback, time, math, random

def log_on_err(f):
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as e:
            eid=str(random.randint(1_000_000, 1_000_000_000))
            msg = str(traceback.format_exc())
            print('ERROR: не сработал парсинг. ошибка:', msg[:200], ' полный лог в error.log с id', eid)
            with open('error.log', 'a+', encoding='utf8') as el:
                el.write(eid + ':' + msg +'\n')
    return wrapper

while True:
    print('останавливать НЕЛЬЗЯ, начался постинг')
    start = time.time()
    parse_failed = False

    log_on_err(parse_main)(pages_amount=Config.amount_of_pages)

    log_on_err(post_main)(amount_of_posts=Config.amount_of_posts)
  
    
    print('останавливать МОЖНО, постинг закончился')    
    time.sleep(abs(Config.interval_seconds - (time.time()-start)))
    
