import scrapy


class MySpider(scrapy.Spider):
    name = 'myspider'

    start_urls = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.info("=" * 50)
        self.initial_params = kwargs.pop('initial_params')
        self.logger.info(self.initial_params)
        self.logger.info("=" * 50)
        self.start_urls += self.initial_params.pop('start_urls')
        self.logger.info("=" * 50)

    def parse(self, response):
        title = response.xpath('/html/head/title').extract()[0]
        self.logger.info("     取得したウェブサイトは '{}' でした".format(title))
        self.logger.info("     {}".format(response.url))

