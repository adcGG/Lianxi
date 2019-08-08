import xml.dom.minidom
document_tree = xml.dom.minidom.parse('storehouse.xml') #解析XML文件
collection = document_tree.documentElement # 把所有元素存入集合中
print(collection.toxml())                  # 打印collection集合内容
goods = collection.getElementsByTagName("goods")        # 获取goods元素下的子元素的集合
goods_record = []
for good_object in goods: # 获取商品记录的详细信息
	if good_object.hasAttribute('category'): # 判断是否存在category属性
		goods_record.append(good_object.getAttribute('category')) # 获取属性对应值
	name = good_object.getElementsByTagName('name')[0] # 获取name标签对应的元素
	goods_record.append(name.childNodes[0].data)   # 获取name元素对应的值
	amount = good_object.getElementsByTagName('amount')[0] # 获取amount标签对应元素
	goods_record.append(amount.childNodes[0].data) # 获取amount标签对应的值
	price = good_object.getElementsByTagName('price')[0] # 获取price标签对应的元素
	goods_record.append(price.childNodes[0].data) # 获取price标签对应的值
print(goods_record)
