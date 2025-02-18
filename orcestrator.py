from poster_annonces import main as post_main
from parser_annonces import main as parse_main
from config import Config
import traceback, time, math

while True:
    print('останавливать НЕЛЬЗЯ, начался постинг')
    start = time.time()
    parse_failed = False

    try:
        parse_main(pages_amount=Config.amount_of_pages)
    except Exception as e:
        print('ERROR: не сработал парсинг. ошибка:', e, traceback.format_exc())
        parse_failed = True

    try:
        post_main(amount_of_posts=Config.amount_of_posts)
    except Exception as e:
        print('ERROR: не сработал парсинг. ошибка:', e, traceback.format_exc())
    
    print('останавливать МОЖНО, постинг закончился')    
    time.sleep(abs(Config.interval_seconds - (time.time()-start)))
    
