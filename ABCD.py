from urllib import response
import scrapy
import psycopg2

#connect to scrap DataBase
conn = psycopg2.connect(
    host="",
    database="scrap",
    user="postgres",
    password="Parisa4653")

    
#Extract Data from webapage
class scraper(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for products in response.css('div.product-item-info'):
            try:
                yield{
                    'name' : products.css('a.product-item-link::text').get(),
                    'price' : products.css('span.price::text').get().replace('£' , ''),
                    'link' : products.css('a.product-item-link').attrib['href'],
                    }
            except:
                yield{
                    'name' : products.css('a.product-item-link::text').get(),
                    'price' : 'Sold Out' . replace(0.00),
                    'link' : products.css('a.product-item-link').attrib['href'],
                    }    

#pagination
        nextpage = response.css('a.action.next').attrib['href']
        if nextpage is not None:
            yield response.follow(nextpage, callback=self.parse)


#load whisky2.scv in product table
cur = conn.cursor()
with open(r"C:\Users\PRS\Desktop\DBproject\scraper\whisky2.csv") as f:
    next(f)
    cur.copy_from(f, 'product', sep=',')

    conn.commit()
            