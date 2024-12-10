import scrapy
import pandas as pd
import random
import time
from fake_useragent import UserAgent

class HockeySpider(scrapy.Spider):
    name = 'hockey_spider'
    start_urls = ['https://www.scrapethissite.com/pages/forms/']

    def parse(self, response):
        # Extracting table rows (skipping the header)
        rows = response.css('table tr')[1:]

        data = []

        for row in rows:
            cols = row.css('td::text').getall()  
            cols = [col.strip() for col in cols]  
            data.append(cols)

        columns = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For (GF)", "Goals Against (GA)", "+ / -"]

        df = pd.DataFrame(data, columns=columns)
        df.to_csv('scraped_data.csv', index=False)
        self.log("Data saved to 'scraped_data.csv'")
