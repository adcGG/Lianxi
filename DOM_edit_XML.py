import xml.dom.minidom
document_tree = xml.dom.minidom.parse('storehouse.xml')
print(document_tree)
collection = document_tree.documentElement # 把所有元素存入集合中
price = collection.getElementsByTagName('price')
price_object = price[0]
price_object.firstChild.data = 8.2
print('修改商品价格成功')
goods = collection.getElementsByTagName('goods')
collection.removeChild(goods[1])
print('节点删除成功（删除第2个goods节点对象）')
f = open('storehouse.xml','w',encoding='utf-8')
f.write(document_tree.toxml())
f.close()