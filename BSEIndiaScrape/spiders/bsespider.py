import scrapy
from ..items import BseindiascrapeItem
from urllib.request import Request


class BsespiderSpider(scrapy.Spider):
    name = 'bsespider'
    #allowed_domains = ['https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx?expandable=3']
    start_urls = ['https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx?expandable=3/']

    def parse(self, response):
        item = BseindiascrapeItem()

        table = response.css('#ContentPlaceHolder1_gvbulk_deals')
        rows = table.css('tr.tdcolumn')
        for row in rows:
            Deal_Date = row.css('.tdcolumn:nth-child(1)::text').extract_first()
            Security_Code= row.css('.tdcolumn:nth-child(2)::text').extract_first()
            Security_Name= row.css('.TTRow_left::text').extract_first()
            Client_Name= row.css('#ContentPlaceHolder1_gvbulk_deals .text-left::text').extract_first()
            Deal_Type= row.css('.text-left+ .tdcolumn::text').extract_first()
            Quantity= row.css('.text-right:nth-child(6)::text').extract_first()
            Price= row.css('#ContentPlaceHolder1_gvbulk_deals .text-right+ .text-right::text').extract_first()


            item['Deal_Date'] = Deal_Date
            item['Security_Code'] = Security_Code
            item['Security_Name'] = Security_Name
            item['Client_Name'] = Client_Name
            item['Deal_Type'] = Deal_Type
            item['Quantity'] = Quantity
            item['Price'] = Price

            yield item

        
