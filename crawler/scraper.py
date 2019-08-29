import scrapy
import re
import time
from read_csv import Read_csv

class GitRepoSpider(scrapy.Spider):
    name = "Github"
    start_urls = Read_csv()
    print(start_urls)

    def parse(self, response):
        for paragraph in response.css('div.Box-body p'):
            for a in paragraph.css('a'):
                title = a.css("::attr(href)").extract_first()
                travis = re.findall("travis", title)
                if(len(travis) > 0):
                    print(str(response) + " true")
                    time.sleep(2)