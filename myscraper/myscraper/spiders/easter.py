import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class EasterSpider(CrawlSpider):
    name = "EasterSpider"
    DOWNLOAD_DELAY = 0.25
    allowed_domains = ["developers.google.com"]
    start_urls = [
        "https://developers.google.com"
    ]

    rules = ( Rule (SgmlLinkExtractor(allow=("", ),),
                callback="parse_items",  follow= True),
    )

    def __init__(self, session_id=-1, *args, **kwargs):
        super(EasterSpider, self).__init__(*args, **kwargs)

    # def parse(self, response):
    #     if "script_foot.js" in response.body:
    #         print "Found easter"
    def parse_items(self, response):
        if "script_foot.js" in response.body:
            print response.url + " found"
        