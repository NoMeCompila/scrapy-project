from scrapy import Selector
from scrapy import Field
from scrapy import Spider
from scrapy import Item
from scrapy.loader import ItemLoader

class Titulo(Item):
    titulo = Field()

class InfobaeSpider(Spider):
    name = "mySpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    start_urls = ['https://www.infobae.com/']

    def parse(self, response):

        sel = Selector(response)
        titulos = sel.xpath("//div[@class='default-chain-ctn']")

        for titulo in titulos:
            item = ItemLoader(Titulo(), titulo)
            item.add_xpath('titulo', './/h2/text()')
            yield item.load_item()