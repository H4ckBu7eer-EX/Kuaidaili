import scrapy
from Kuaidaili.item import KuaidailiItem

class KuaidailipositionSpider(scrapy.Spider):
    name = 'kuaidailiPosition'
    allowed_domains = ['kuaidaili.com']
    url = "https://www.kuaidaili.com/free/inha/"
    offset = 1

    start_urls = [url+str(offset)]

    def parse(self, response):
        #FROM H4CKHU7EER
        for line in response.xpath("//tr[@class='table table-bordered table-striped']"):
            item = KuaidailiItem()
            item['position_ip'] = line.xpath("./td[1]/text()").extract()[0]
            item['position_port'] = line.xpath("./td[2]/text()").extract()[0]
            item['position_niming'] = line.xpath("./td[3]/text()").extract()[0]
            item['position_yp'] = line.xpath("./td[4]/text()").extract()[0]
            item['position_loc'] = line.xpath("./td[5]/text()").extract()[0]
            item['position_spe'] = line.xpath("./td[6]/text()").extract()[0]
            item['position_time'] = line.xpath("./td[7]/text()").extract()[0]
            yield item



        if self.offset < 10:
            self.offset = self.offset +1

        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)    
