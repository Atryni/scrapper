from tinydb import TinyDB
from app.scrappers.rss import RssScrapper

db = TinyDB('db.json')

if __name__ == "__main__":
    rss = RssScrapper()
    rss.job()
    print('Done.')
