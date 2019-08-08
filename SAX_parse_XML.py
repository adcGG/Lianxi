import xml.sax
import sys
get_record = [] # 全局列表变量，准备接收获取的XML的内容
class GetStorehouse(xml.sax.ContentHandler):  #自定义获取仓库商品类（事件处理器）
	def __init__(self):
		self.CurrentData = "" # 自定义当前元素标签名属性
		self.title = "" # 自定义商品二级分类属性
		self.name = "" # 自定义商品名称内容属性
		self.amount = "" # 自定义商品数量内容属性
		self.price = "" # 自定义商品价格内容属性
	def startElement(self,label,attributes): # 遇到元素开始标签时，触发该函数
		self.CurrentData = label
		if label == "goods":
			category = attributes["category"]
			return category
	def endElement(self,label):
		global get_record
		if self.CurrentData == 'title':
			get_record.append(self.title)
		elif self.CurrentData == 'name':
			get_record.append(self.name)
		elif self.CurrentData == 'amount':
			get_record.append(self.amount)
		elif self.CurrentData == 'price':
			get_record.append(self.price)
	def characters(self,content):
		if self.CurrentData == 'title':
			self.title = content
		elif self.CurrentData == 'name':
			self.name = content
		elif self.CurrentData == 'amount':
			self.amount = content
		elif self.CurrentData == 'price':
			self.price = content

#================================================================

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)
Handler = GetStorehouse()
parser.setContentHandler(Handler)
parser.parse("storehouse.xml")
print(get_record)

