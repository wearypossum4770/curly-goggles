# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from scrapy.exporters import PythonItemExporter,JsonLinesItemExporter

class FloridaHillsPipeline:
	def process_item(self, item, spider):
		exporter = self.JsonItemExporter(item)
		exporter.export_item(item)
		return item

