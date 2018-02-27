from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hakka import Hakka
from crochet import setup, wait_for
from os import environ

setup()
app = Hakka()
process = CrawlerProcess(get_project_settings())


@wait_for(timeout=5.0)
@app.watch('scrapy:myspider', redis_dtype='list', redis_vtype='json')
def start_crawl(spider_name=None, initial_params=None, *args, **kwargs):
    print("Hello! start_crawl")
    print(initial_params)
    process.crawl(spider_name, initial_params=initial_params)


app.listen(host=environ.get('REDIS_HOST', 'localhost'), port=environ.get('REDIS_PORT', 6379),
           db=environ.get('REDIS_DB', 0), debug=True)
