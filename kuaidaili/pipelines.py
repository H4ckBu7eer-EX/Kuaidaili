# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class KuaidailiPipeline:
    def __init__(self):
        self.filename = open("kuaidaili.json","w")

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii = False) + "\n"
        self.filename.write(str(text))
        return item

    def clsoe_spider(self,spider):
        self.filename.clsoe()   
