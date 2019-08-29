import scrapy
import re
import time
import csv
from bs4 import BeautifulSoup
from read_csv import Read_csv

class GitRepoSpider(scrapy.Spider):
    name = "Github"
    urls = Read_csv.repo_github()
    start_urls = []
    for url in urls:
        start_urls.append("https://github.com/" + url)

    def save_to_csv(response):
        with open('results.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(response)
        csvFile.close()

    def parse(self, response):
        f = open("results.txt","a+")
        for paragraph in response.css('div.Box-body p'):
            for a in paragraph.css('a'):
                title = a.css("::attr(href)").extract_first()
                travis = re.findall("travis", title)
                if(len(travis) > 0):
                #     with open('results.csv', 'a') as csvFile:
                #         # soup = BeautifulSoup(response.url)
                    f.write(response.url.replace(',','') + " true\n")
                    time.sleep(2)
        f.close()
