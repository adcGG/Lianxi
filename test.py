# # import os
# # # from datetime import datetime,date,time
# # # filename = 'test.txt'
# # # filepath = os.getcwd()+'\\'+filename
# # # newfile = open(filepath,'w')
# # # newfile.write('zzn\n')
# # # newfile.write('nianl\n')
# # # newfile.write(str(datetime.now()))
# # # newfile.close()
# # # print('OK')
# from datetime import datetime,date,time
# import time
# import random


# import requests
# import multiprocessing
# from requests.exceptions import ConnectionError
# def scrape(url):
# 	try:
# 		print("爬取%s成功！收到%s"%(url,requests.get(url)))
# 	except ConnectionError:
# 		print("爬取%s出错！"%(url))
#
# if __name__=="__main__":
# 	pool = multiprocessing.Pool()
# 	urls = [
# 		'http://www.metro.cn/',
# 		'http://www.shuichan.cc/',
# 		'http://www.51sole.com/',
# 		'http://www.x009.com/',
# 		'http://www.x009.comd/'
# 	]
# 	pool.map(scrape,urls)

# import urllib.request
# #response 为响应对象
# response = urllib.request.urlopen('http://www.baidu.com/')
# html = response.read().decode("utf-8")
# print(type(html))
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE

# import urllib.request
# url = 'http://www.baidu.com/'
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
# # 1.创建请求对象（User-Agent)
# req = urllib.request.Request(url,headers=headers)
#
# # 2.获取响应对象（urlopen()）
# res = urllib.request.urlopen(req)
#
# # 3.响应对象read().decode("utf-8")
# html = res.read().decode("utf-8")
# # print(html)
# print(res.getcode())
# print(res.geturl())

# import urllib.request
# import urllib.parse
# baseurl = 'http://www.baidu.com/s?'
# key = input("请输入要搜索的内容：")
# # 进行urlencode()编码
# wd = {"wd":key}
# key = urllib.parse.urlencode(wd)
# url = baseurl+key
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
# # 创建请求对象
# req = urllib.request.Request(url,headers=headers)
# # 获取响应对象
# res = urllib.request.urlopen(req)
# html = res.read().decode("utf-8")
# # 写入本地文件
# with open("搜索.txt","w",encoding="gb18030") as f:
# 	f.write(html)

# import urllib.request
# import urllib.parse
# import random
# import time
#
# header_list = [{"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"},
#                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
#                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}]
# headers = random.choice(header_list)
#
# baseurl = 'https://tieba.baidu.com/f?'
# # 主体程序
# name = input("输入贴吧名称：")
# begain = int(input("请输入起始页码："))
# end = int(input("请输入结尾页码："))
#
# kw = {"kw":name}
# kw = urllib.parse.urlencode(kw)
# file = r"D:\pythonlearning\lianxi\tieba\a"
# # 拼接URL发请求，获取响应
# for i in range(begain,end+1):
# 	# 拼接URL
# 	pn = (i-1)*50
# 	url = baseurl+kw+'&pn='+str(pn)
# 	# 发起请求
# 	time.sleep(2)
# 	req = urllib.request.Request(url,headers=headers)
# 	res = urllib.request.urlopen(req,timeout=5) # 等待5秒钟，超时结束
# 	html = res.read().decode("utf-8")
# 	# 写入文件
# 	filename = file+"第"+str(i)+'页.html'
# 	print(filename)
# 	with open(filename,'w',encoding="utf-8") as f:
# 		print("正在爬取第%d页"%i)
# 		f.write(html)
# 		print("爬取第%d成功" % i)

# import urllib.request
# import urllib.parse
# import random
# import time
#
# header_list = [{"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"},
#                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
#                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}]
#
#
# # 读取页面
# def readPage(url):
# 	headers = random.choice(header_list)
# 	req = urllib.request.Request(url,headers=headers)
# 	res = urllib.request.urlopen(req,timeout=5)
# 	html = res.read().decode("utf-8")
# 	return html
#
# # 写入文件
# def writePage(filename,html):
# 	with open(filename,'w',encoding="utf-8") as f:
# 		f.write(html)
#
# # 主函数
# def workOn():
# 	name = input("输入贴吧名称：")
# 	begain = int(input("请输入起始页码："))
# 	end = int(input("请输入结尾页码："))
# 	baseurl = 'https://tieba.baidu.com/f?'
# 	kw = {"kw":name}
# 	kw = urllib.parse.urlencode(kw)
# 	file = r"D:\pythonlearning\lianxi\tieba\a"
# 	# 拼接URL发请求，获取响应
# 	for i in range(begain,end+1):
# 		# 拼接URL
# 		pn = (i-1)*50
# 		url = baseurl+kw+'&pn='+str(pn)
# 		# 发起请求
# 		time.sleep(2)
# 		html = readPage(url)
# 		filename = file + "第" + str(i) + '页.html'
# 		writePage(filename,html)
#
#
#
# if __name__=='__main__':
# 	workOn()

# import urllib.request
# import urllib.parse
# import json
# # 请输入你要翻译的内容
# key = input("请输入你要翻译的内容:")
#
# data = {"i": key,
# 		"from": "AUTO",
# 		"to": "AUTO",
# 		"smartresult": "dict",
# 		"client": "fanyideskweb",
# 		"salt": "15636915296183",
# 		"sign": "169489d0ce19ebec1942c2f2516edd99",
# 		"ts": "1563691529618",
# 		"bv": "97ba7c7fb78632ae9b11dcf6be726aee",
# 		"doctype": "json",
# 		"version": "2.1",
# 		"keyfrom": "fanyi.web",
# 		"action": "FY_BY_REALTlME",
#         }
#
# data = urllib.parse.urlencode(data)
# # data:
# # i=%E7%8E%8B%E8%80%85&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=15636
# # 915296183&sign=169489d0ce19ebec1942c2f2516edd99&ts=1563691529618&bv=97ba7c7fb78632ae9b
# # 11dcf6be726aee&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTlME
# data = bytes(data,encoding="utf-8")
# # 发请求，获取响应
# # url为POST的地址，可以F12 看header里的内容 Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
# # 这里有道词典要去掉 translate_o 的 _o ，其他的不用
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
#
# req = urllib.request.Request(url,data=data,headers=headers)
# res = urllib.request.urlopen(req)
# html = res.read().decode("utf-8")
# # print(html,type(html)) # html是字符串str
# # 把json格式字符串str转化为字典dict
# r_dict = json.loads(html)
# translateResult = r_dict["translateResult"][0][0]["tgt"]
# print(translateResult)


# import re
# s = '''<div><p>仰天大笑出门去</p></div>
# 		<div><p>窗前明月光</p></div>'''
# # 创建编译对象,贪婪匹配 .*
# p = re.compile('<div><p>.*</p></div>',re.S) # re.S使 . 能够匹配全文字符，包括\n
# # 非贪婪匹配 .*?
# p1 = re.compile('<div><p>.*?</p></div>',re.S)
# # 匹配字符串
# r = p.findall(s)
# r1 = p1.findall(s)
# print(r)
# print('r1',r1)

# import re
# s = "A B C D"
# # 分组：先按照整体匹配出来，然后再匹配()中的
# # 如果有2个或多个(),则以元组方式去显示
# p1 = re.compile('\w+\s+\w+')
# print(p1.findall(s))
# p2 = re.compile('(\w+)\s+\w+')
# # 第1步： ['A B','C D']
# # 第2步： ['A','C']  在'A B'中匹配，显示括号的内容
# print(p2.findall(s))
# p3 = re.compile('(\w+)\s+(\w+)')
# print(p3.findall(s))
# p4 = re.compile('\w+(\s+)\w+')
# print(p4.findall(s))
# p5 = re.compile('(\w+)(\s+)(\w+)')
# print(p5.findall(s))


# import re
# s = '''
# 	<div class="animal">
# 		<p class="name">
# 			<a title="Tiger"></a>
# 		</p>
# 		<p class="contents">
# 			Two tigers two tigers run fast
# 		</p>
# 	</div>
# 	<div class="animal">
# 		<p class="name">
# 			<a title="Rabbit"></a>
# 		</p>
# 		<p class="contents">
# 			rabbit is so white
# 		</p>
# 	</div>
# '''
# # .*class="contents">\s+(\w+)\s+</p>.*
# tiger = re.compile(r'title="(\w+)"></a>\s+</p>\s+<p class="contents">\s+([\w+ ]+)')
# tiger_r = tiger.findall(s)
# p = re.compile('<div class="animal".*?title="(.*?)">.*?contents">\s+([\w+ ]+)',re.S)
# r = p.findall(s)
# print(tiger_r)
# print(r)
# for animal in r:
# 	print("动物名称：",animal[0].strip())
# 	print("动物描述：", animal[1].strip())
# [("Tiger","Two tiger..",
# ("Rabbit","rab...")]
# 打印输出
# 动物名称
# 描述

# csv使用
# import csv
# with open("猫眼.csv",'a',newline="") as f:
# 	# 初始化写入对象
# 	writer = csv.writer(f)
# 	# 把列表写入文件中
# 	writer.writerow(["霸王别姬","张国荣"]) # 这里默认有个\n所以有个空行，所以需要添加newline=“”
# 	writer.writerow(["唐伯虎点秋香", "周星驰"])


# import urllib.request
# import urllib.parse
# import re
# import random
# import time
# import csv
#
# header_list = [{"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"},
#                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
#                {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}]
#
# class MaoyanSpider:
# 	def __init__(self):
# 		self.baseurl = "https://maoyan.com/board/4?offset="
# 		self.headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
# 		self.page = 1
# 		self.offset = 0
# 	def loadPage(self,url):
# 		req = urllib.request.Request(url,headers=self.headers)
# 		res = urllib.request.urlopen(req)
# 		result = res.read().decode("utf-8")
# 		self.parsePage(result)
#
# 	def parsePage(self,result):
# 		p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">\s+(.*?)\s+</p>.*?releasetime">(.*?)</p>',re.S)
# 		r_list = p.findall(result)
# 		#[("电影名称","主演","1994-01-01")]
# 		print("r_list",r_list)
# 		self.writePage(r_list)
#
# 	def writePage(self,r_list):
# 		for r_tuple in r_list:
# 			with open("猫眼电影.csv", 'a',newline="", encoding="gb18030") as f:
# 				writer = csv.writer(f)
# 				L = list(r_tuple)
# 				writer.writerow(L)
# 	def workOn(self):
# 		self.loadPage(self.baseurl)
# 		print("爬取猫眼电影")
# 		while True:
# 			if self.page == 10:
# 				print("爬取完成，退出了")
# 				break
# 			choice = input("爬取请按（y/n)：")
# 			if choice.strip().lower() =="y":
# 				self.page += 1
# 				self.offset = (self.page-1)*10
# 				url = self.baseurl+str(self.offset)
# 				self.loadPage(url)
#
# 			else:
# 				print("爬取结束，谢谢使用")
# 				break
#
# if __name__=="__main__":
# 	with open("猫眼电影.csv", 'w', newline="", encoding="gb18030") as f:
# 		writer = csv.writer(f)
# 		L = ['电影名称','主演','上映时间']
# 		writer.writerow(L)
# 	spider = MaoyanSpider()
#
# 	spider.workOn()

# import requests
# url = 'http://www.baidu.com/'
# headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
# response = requests.get(url,headers=headers)
# # 获取响应内容
# # print(response.text)
# # print(response.encoding)
# # 默认返回编码格式，ISO-8859-1
# response.encoding = "utf-8"
# # 获取字符串str
# # print(response.text)
# # 获取字节流bytes
# # print(response.content)
# # 返回服务器响应码
# print(response.status_code)
# # 返回数据的URL
# print(response.url)

# import requests
# baseurl = 'http://www.baidu.com/s?'
# key = input("请输入要搜索的内容：")
# # 进行urlencode()编码
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
# params = {"wd":key}
# # 自动编码，自动拼接URL，params必须为字典
# res = requests.get(baseurl,params=params,headers=headers)
# # 一般要指定字符编码utf-8
# res.encoding = "utf-8"
# print(res.text)

# import urllib.request
# import urllib.parse
# import json
# import requests
# # 请输入你要翻译的内容
# key = input("请输入你要翻译的内容:")
#
# data = {"i": key,
# 		"from": "AUTO",
# 		"to": "AUTO",
# 		"smartresult": "dict",
# 		"client": "fanyideskweb",
# 		"salt": "15636915296183",
# 		"sign": "169489d0ce19ebec1942c2f2516edd99",
# 		"ts": "1563691529618",
# 		"bv": "97ba7c7fb78632ae9b11dcf6be726aee",
# 		"doctype": "json",
# 		"version": "2.1",
# 		"keyfrom": "fanyi.web",
# 		"action": "FY_BY_REALTlME",
#         }
# # 发请求，获取响应
# # url为POST的地址，可以F12 看header里的内容 Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
# # 这里有道词典要去掉 translate_o 的 _o ，其他的不用
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
# headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
#
# res = requests.post(url,data=data,headers=headers)
# res.encoding = "utf-8"
# html = res.text
# r_dict = json.loads(html)
# translateResult = r_dict["translateResult"][0][0]["tgt"]
# print(translateResult)


# import requests
# import random
# import time
# import csv
# import re
# import pymysql,sys
# #data-is_focus="" data-sl="">融湖中心城二期 3室2厅 370万</a>
#
# class SecondHouseSpider:
# 	def __init__(self):
# 		self.baseurl = "https://sz.lianjia.com/ershoufang/pg"
# 		self.header_list = [{"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"},
# 		               {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
# 		               {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}]
# 		self.headers = random.choice(self.header_list)
# 		self.page = 1
# 	def loadPage(self,url):
# 		res = requests.get(url,headers = self.headers)
# 		res.encoding = "utf-8"
# 		result = res.text
# 		self.parsePage(result)
#
# 	def parsePage(self,result):
# 		p = re.compile(
# 			'<div class="title">.*?data-is_focus="" data-sl="">(.*?)</a>.*?data-el="region">(.*?)</a>(.*?)</div>'
# 			'.*?</span>(.*?)<a href.*?blank">(.*?)</a>.*?</span>(.*?)</div>.*?<span>(.*?)</span>.*?<span>(.*?)</span>',
# 			re.S)
# 		r_list = p.findall(result)
# 		#[("电影名称","主演","1994-01-01")]
# 		print("r_list",r_list)
# 		self.writePage(r_list)
#
# 	def writePage(self,r_list):
# 		for r_tuple in r_list:
# 			with open("二手房信息.csv", 'a',newline="", encoding="gb18030") as f:
# 				writer = csv.writer(f)
# 				L = list(r_tuple)
# 				writer.writerow(L)
# 	def workOn(self):
# 		self.loadPage(self.baseurl)
# 		print("爬取二手房信息")
# 		while True:
# 			if self.page > 30:
# 				print("爬取完成，退出了")
# 				break
# 			else:
# 				self.page += 1
# 				url = self.baseurl+str(self.page)+'/'
# 				time.sleep(random.uniform(1.5,4))
# 				self.loadPage(url)
#
#
# if __name__=="__main__":
# 	with open("二手房信息.csv", 'w', newline="", encoding="gb18030") as f:
# 		writer = csv.writer(f)
# 		L = ['房名信息', '地点', '房屋情况', '房源情况', '所在地区', '关注/发布时间', '价格（万）', '单价']
# 		writer.writerow(L)
# 	spider = SecondHouseSpider()
# 	spider.workOn()



# import requests
# url = "http://www.baidu.com/"
# proxies = {"http":"http://222.189.191.226:9999"}
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"}
# res = requests.get(url,proxies=proxies,headers=headers)
# print(res.status_code)


# import requests
# import random
# import time
# import csv
# import re
# import pymysql,sys,pymongo
# #data-is_focus="" data-sl="">融湖中心城二期 3室2厅 370万</a>
#
# class SecondHouseSpider:
# 	def __init__(self):
# 		self.baseurl = "https://sz.lianjia.com/ershoufang/pg"
# 		self.header_list = [{"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"},
# 		               {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"},
# 		               {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}]
# 		self.headers = random.choice(self.header_list)
# 		self.page = 1
#
# 	def connectMongo(self):
# 		try:
# 			self.conn = pymongo.MongoClient('localhost',27017 )
# 			self.spiderdb = self.conn.spiderdb
# 			self.myset = self.spiderdb.SecondHouse
# 			print('数据库这里连接成功了')
# 		except:
# 			print("打开数据库连接出错，请检查！")
# 			self.conn.close()
# 			sys.exit()
#
# 	def closeMongo(self):
# 		self.conn.close()  # 创建数据库操作类的实例
#
# 	def loadPage(self,url):
# 		res = requests.get(url,headers = self.headers)
# 		res.encoding = "utf-8"
# 		result = res.text
# 		self.parsePage(result)
#
# 	def parsePage(self,result):
# 		p = re.compile(
# 			'<div class="title">.*?data-is_focus="" data-sl="">(.*?)</a>.*?data-el="region">(.*?)</a>(.*?)</div>'
# 			'.*?</span>(.*?)<a href.*?blank">(.*?)</a>.*?</span>(.*?)</div>.*?<span>(.*?)</span>.*?<span>(.*?)</span>',
# 			re.S)
# 		r_list = p.findall(result)
# 		#[("电影名称","主演","1994-01-01")]
# 		self.writePage(r_list)
#
# 	def writePage(self,r_list):
# 		self.connectMongo()
# 		for r_tuple in r_list:
# 			self.myset.insert([{"Housing_Introduction":r_tuple[0],
# 			                    "Place":r_tuple[1],
# 			                    "Housing_Situation":r_tuple[2],
# 			                    "Floor_Location":r_tuple[3],
# 			                    "Location":r_tuple[4],
# 			                    "Follow":r_tuple[5],
# 			                    "Price":r_tuple[6]+'万元',
# 			                    "Unit_Price":r_tuple[7],}])
#
# 		self.closeMongo()
# 	def workOn(self):
# 		self.loadPage(self.baseurl)
# 		print("爬取二手房信息")
# 		while True:
# 			if self.page > 2:
# 				print("爬取完成，退出了")
# 				break
# 			else:
# 				self.page += 1
# 				url = self.baseurl+str(self.page)+'/'
# 				time.sleep(random.uniform(1.5,4))
# 				self.loadPage(url)
# if __name__=="__main__":
# 	spider = SecondHouseSpider()
# 	spider.workOn()

# import requests
# import re
#
# class NoteSpider:
# 	def __init__(self):
# 		self.headers = {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
# 		self.url = "http://code.tarena.com.cn/"
# 		self.proxies = {"http":"http://163.125.223.119:8118"}
# 		# 用户名和密码必须为元组
# 		self.auth = ("tarenacode","code_2013")
#
# 	def getParsePage(self):
# 		res = requests.get(self.url,
# 		                   proxies = self.proxies,
# 		                   headers = self.headers,
# 		                   auth = self.auth,
# 		                   timeout = 5)
# 		res.encoding = "utf-8"
# 		html = res.text
# 		print(html)
# 		p = re.compile('<a href=".*?">(.*?)</a>',re.S)
# 		r_list = p.findall(html)
# 		print(r_list)
# 		self.writePage(r_list)
# 	def writePage(self,r_list):
# 		print("开始写入文件")
# 		with open("达内科技.txt",'a') as f:
# 			for r_str in r_list:
# 				f.write(r_str+'\n\n')
# if __name__=="__main__":
# 	spider = NoteSpider()
# 	spider.getParsePage()


# import requests
#
# url = "https://www.12306.cn/mormhweb/"
# headers = {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
# res = requests.get(url,headers=headers,verify = False)
# res.encoding = "utf-8"
# print(res.text)

# import urllib.request
# url = "http://www.baidu.com/"
# headers = {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}
# # 创建Handler处理器对象
# http_handler = urllib.request.HTTPHandler()
# # proxier_handler = urllib.request.ProxyHandler()
# # 创建自定义的opener对象
# opener = urllib.request.build_opener(http_handler)
# # 利用opener对象的open()方法发起请求
# req = urllib.request.Request(url)
# res = opener.open(req)
# print(res.read().decode("utf-8"))




# from lxml import etree
# with open('html.txt','r',encoding="gb18030") as f:
# 	html = f.read()
# # 构造解析对象
# parseHtml = etree.HTML(html)
# # 利用解析对象调用xpath匹配
# r1 = parseHtml.xpath('//li[@data-groupid="107"]/a/@href')
# r2 = parseHtml.xpath('//li[@data-groupid="107"]/a/text()')
# print(r1,r2)
# for i in range(101,117):
# 	r3 = parseHtml.xpath('//li[@data-groupid="'+str(i)+'"]/a/text()')
# 	print('i = ',i,r3,r3.text)


#
# import requests,os,sys,time,random
# from lxml import etree
#
# class BaiduImageSpider:
# 	def __init__(self):
# 		self.url = "https://tieba.baidu.com/f?"
# 		self.params = {'kw':'','pn':'0'}
# 		self.page = 1
# 		self.baseurl = 'https://tieba.baidu.com'
# 	# 获取所有帖子URL列表
# 	def getPageUrl(self):
# 		res = requests.get(self.url,params=self.params)
# 		res.encoding = "utf-8"
# 		html = res.text
# 		parsehtml = etree.HTML(html)
# 		TieziUrl = parsehtml.xpath('//a[@class="j_th_tit "]/@href')
# 		for link in TieziUrl:
# 			self.getImageUrl(link)
# 	# 获取帖子中图片URL列表
# 	def getImageUrl(self,link):
# 		url = self.baseurl+link
# 		time.sleep(random.uniform(1.6,6))
# 		res = requests.get(url)
# 		res.encoding="utf-8"
# 		html = res.text
# 		parseImageUrl = etree.HTML(html)
# 		tupianUrl = parseImageUrl.xpath('//img[@class="BDE_Image"]/@src')
# 		for jpgurl in tupianUrl:
# 			self.writeImage(jpgurl)
#
# 	# 下载图片到本地文件
# 	def writeImage(self,jpgurl):
# 		res = requests.get(jpgurl)
# 		l = len(jpgurl)
# 		file = r"D:\pythonlearning\lianxi\tieba\tie"+self.params['kw']
# 		filename = r"D:\pythonlearning\lianxi\tieba\tie"+self.params['kw']+r"\a"+jpgurl[l-10:]
# 		try:
# 			if not os.path.isdir(file):
# 				os.makedirs(file)
# 		except:
# 			print("子文件夹%s建立出错"%file)
# 			sys.exit()
# 		html = res.content
# 		with open(filename,'wb')as f:
# 			f.write(html)
# 	def workOn(self):
# 		key = input("请输入要查找的贴吧名称：")
# 		start = int(input("开始的页码为："))
# 		end = int(input("结束的页码为："))
# 		for i in range(start,end+1):
# 			self.page = (i-1)*50
# 			self.params['kw'] = key
# 			self.params['pn'] = str(self.page)
# 			print("现在开始爬取第%d"%(self.page+1),'页')
# 			self.getPageUrl()
# 			print("爬取完成！")
#
# if __name__=="__main__":
# 	jpgSpider = BaiduImageSpider()
# 	jpgSpider.workOn()
##################################################################
# import json
# jsarry = '[1,2,3,4,5]'
# L =json.loads(jsarry)
# print(type(L),L)
# # json格式的对象
# jsonobj ='{"city":"天地会","name":"步惊云"}'
# D = json.loads(jsonobj)
# print(type(D),D)
# L1 = [1,2,3,4,5]
# L2 = (3,4,6,5,7)
# D1 = {"city":"天地会","name":"聂风"}
# jsarry1 = json.dumps(L1)
# jsarry2 = json.dumps(L2)
# jsonobj1 = json.dumps(D1,ensure_ascii=False)
# print(type(jsarry1),jsarry1)
# print(type(jsarry2),jsarry2)
# print(type(jsonobj1),jsonobj1)


# import requests
# import json
# import csv
# import re
# url_types = 'https://movie.douban.com/chart'
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) ASD'}
# typenum = ''
# typename = ''
# res_types = requests.get(url_types,headers=headers)
# res_types.encoding = "utf-8"
# html_types = res_types.text
# find_types = re.compile('.*?type_name=(.*?)&type=(.*?)&',re.S)
# type_sesult = find_types.findall(html_types)
# a = []
# for i in range(len(type_sesult)):
# 	a.append(type_sesult[i][0])
# print("分类类型有：",','.join(a))
# flag = True
# while flag:
# 	typename = input("请从上面的分类类型里，选择一个类型进行排行榜的查找：")
# 	typenum = None
# 	for i in range(len(a)):
# 		if typename==a[i]:
# 			typenum = type_sesult[i][1]
# 			break
# 	flag = False
# 	if typenum==None:
# 		print("没有找到该类型,请检查")
# 		flag = True
# # url要写抓到的GET
# url = 'https://movie.douban.com/j/chart/top_list?'
# num = input("请输入要爬取的数量：")
# params ={
# 	"type":	typenum,
# 	"interval_id":"100:90",
# 	"action":"",
# 	"start":"0",
# 	"limit":num,
# 	}
# res = requests.get(url,params=params,headers = headers)
# res.encoding = "utf-8"
# # html 是json格式的数组
# html = res.text
# # 数组->列表
# html = json.loads(html)
# # 用for循环遍历每个电影信息{}
# with open("豆瓣电影"+typename+"的排名.csv", 'w', newline='') as f:
# 	writer = csv.writer(f)
# 	L = ['rank','score', 'types','regions','title','actors']
# 	writer.writerow(L)
# for film in html:
# 	name = film['title']
# 	score = film['score']
# 	types = ','.join(film['types'])
# 	regions = ','.join(film['regions'])
# 	rank  = film['rank']
# 	actors = ','.join(film['actors'])
# 	with open("豆瓣电影"+typename+"的排名.csv",'a',newline='',encoding="gb18030") as f:
# 		writer =csv.writer(f)
# 		L = [rank,score,types,regions,name,actors]
# 		writer.writerow(L)
# print("爬取完成！")

# # 导入selenium库中的webdriver
# from selenium import webdriver
# # 创建phantomjs浏览器对象
# driver = webdriver.PhantomJS()
# # 发请求 get()
# driver.get("http://www.baidu.com/")
# # 获取网页截屏
# driver.save_screenshot("百度.png")
# print("图片截取成功")
# driver.quit()


# # 导入selenium库中的webdriver
# from selenium import webdriver
# import time
# # 创建phantomjs浏览器对象
# driver = webdriver.PhantomJS()
# # 发请求 get()  打开页面
# driver.get("http://www.baidu.com/")
# # 发送文字到搜索框
# kw = driver.find_element_by_id("kw")
# kw.send_keys("刺客信条")
# # 点击“百度一下”
# su = driver.find_element_by_id("su")
# su.click()
# # 获取网页截屏
# time.sleep(2)
# driver.save_screenshot("刺客信条搜索.png")
# print("图片截取成功")
# # 关闭浏览器
# driver.quit()

# '''09_selenium+Chrome登陆豆瓣案例.py'''
# from selenium import webdriver
# import time
#
# # 创建浏览器对象,发请求
# driver = webdriver.Chrome()
# driver.get("https://www.douban.com/")
# time.sleep(0.5)
# # 获取截图(验证码)
# driver.save_screenshot("验证码.png")
# # 找 用户名、密码、验证、登陆豆瓣按钮
# uname = driver.find_element_by_name("form_email")
# uname.send_keys("13723426466")
# # 密码
# pwd = driver.find_element_by_name("form_password")
# pwd.send_keys("979818137zzn")
# # 验证码
# key = input("请输入验证码：")
# yzm = driver.find_element_by_id("captcha_field")
# yzm.send_keys(key)
# driver.save_screenshot("完成.png")
# # 点击登陆按钮
# login = driver.find_element_by_class_name("bn-submit")
# login.click()
# time.sleep(1)
# driver.save_screenshot("登陆成功.png")
# # 关闭浏览器
# driver.quit()


# # 操作键盘
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver
# import time
# # 创建浏览器对象，发请求
# driver = webdriver.PhantomJS()
# # 发请求 get()
# driver.get("http://www.baidu.com/")
# # 百度搜索框输入python
# kw = driver.find_element_by_id("kw")
# kw.send_keys("python")
# driver.save_screenshot("01输入python.png")
# # 全选：ctrl+a
# kw = driver.find_element_by_id("kw")
# kw.send_keys(Keys.CONTROL,'a')
# driver.save_screenshot("02全选.png")
# # 剪切：ctrl+x
# kw = driver.find_element_by_id("kw")
# kw.send_keys(Keys.CONTROL,'x')
# driver.save_screenshot("03剪切.png")
# # 粘贴：ctrl+v
# kw = driver.find_element_by_id("kw")
# kw.send_keys(Keys.CONTROL,'v')
# driver.save_screenshot("04粘贴.png")
# # 清空搜索框，对象名，clear方法
# kw = driver.find_element_by_id("kw")
# kw.clear()
# driver.save_screenshot("05清空搜索框.png")
# # 输入：刺客信条
# kw = driver.find_element_by_id("kw")
# kw.send_keys("刺客信条")
# driver.save_screenshot("06输入刺客信条.png")
# # 输入回车
# kw = driver.find_element_by_id("kw")
# kw.send_keys(Keys.ENTER)
# time.sleep(1)
# driver.save_screenshot("07回车.png")
# # 关闭
# driver.quit()

# from selenium import webdriver
# from lxml import etree
# import time
#
# # 打开chrome的方式
# # options = webdriver.ChromeOptions()
# # options.binary_location = r"C:\Program Files (x86)\ChromeCore\ChromeCoreLauncher.exe"
# # browser = webdriver.Chrome(options=options)
#
# # 把Chrome设置无界面浏览器
# opt= webdriver.ChromeOptions()
# opt.binary_location=r"C:\Program Files (x86)\ChromeCore\ChromeCore.exe"
# opt.set_headless()
#
# # 创建浏览器对象
# driver = webdriver.Chrome(options=opt)
#
# driver.get('https://www.douyu.com/directory/all')
# print("登录网址")
# print(type(driver.page_source))
# driver.page_source.encode(encoding = 'utf-8')
# # driver.save_screenshot("登录斗鱼.png")
# # f = open('斗鱼html.txt','w',encoding='utf-8')
# # f.write(driver.page_source)
# # f.close()
# print(type(driver.page_source))
# # 循环
# while True:
# 	# 解析（driver.page_source)
# 	# 获取主播名称，和观众人数
# 	parseHtml = etree.HTML(driver.page_source)
# 	names = parseHtml.xpath('//h2[@class="DyListCover-user"]/text()')
# 	numbers = parseHtml.xpath('//span[@class="DyListCover-hot"]/text()')
# 	for name,number in zip(names,numbers):
# 		print('主播名称：%s，观众人数：%s'%(name,number))
# 		# >>> L1 = [1,2,3]
# 		# >>> L2 = ['A','B','C']
# 		# >>> L3 = zip(L1,L2)
# 		# L3 [(1,'A'),(2,'B'),(3,'C')]
# 		#>>> for i,j in L3:
# 		# ...     print(i,j)
# 		# ...
# 		# 1 A
# 		# 2 B
# 		# 3 C
# 	# 判断是否需要点击下一页
# 	if driver.page_source.find('aria-disabled="false"'):
# 		print("找到下一页")
# 		driver.find_element_by_class_name('dy-Pagination-next').click()
# 		print("==============进入下一页了======================")
# 		time.sleep(2)
# 	else:
# 		break
# driver.close()
	# 没有下一页< li title = "下一页"class ="dy-Pagination-disabled dy-Pagination-next" aria-disabled="true" > < span class ="dy-Pagination-item-custom xh-highlight" > 下一页 < / span > < / li >
# 有下一页<li title="下一页" class=" dy-Pagination-next" aria-disabled="false" tabindex="0"><span class="dy-Pagination-item-custom xh-highlight">下一页</span></li>

# from selenium import webdriver
# import time
# import csv
#
# pdt = input("请输入要爬取的商品：")
#
# opt= webdriver.ChromeOptions()
# opt.binary_location=r"C:\Program Files (x86)\ChromeCore\ChromeCore.exe"
# driver = webdriver.Chrome(options=opt)
# driver.get('https://www.jd.com/')
#
# text = driver.find_element_by_class_name('text')
# text.send_keys(pdt)
#
# button = driver.find_element_by_class_name('button')
# button.click()
# time.sleep(1)
# i = 1
# flag = True
# with open("商品.csv", 'w', newline='', encoding='gb18030') as f:
# 	writer = csv.writer(f)
# 	L = ['name', 'price', 'commit', 'market']
# 	writer.writerow(L)
# while flag:
# 	driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# 	time.sleep(2)
# 	r_list = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
# 	print(r_list)
# 	for r in r_list:
# 		m = r.text.split('\n')
# 		# ['￥40.0','Python...','',]
# 		price = m[0]
# 		name = m[1]
# 		commit = m[2]
# 		market = m[3]
# 		with open("商品.csv",'a',newline='',encoding='gb18030') as f:
# 			writer = csv.writer(f)
# 			L = [name.strip(),price.strip(),commit.strip(),market.strip()]
# 			writer.writerow(L)
# 	y_n = input("第%d页爬取成功,是否爬取下一页(y/n)："%i)
# 	if y_n.strip() == 'y':
# 		flag = True
# 	else:
# 		flag = False
# 		i+=1
# f.close()
# driver.close()



# import requests
# from lxml import etree
# from queue import Queue
# import threading
# import time
#
# class bsSpider:
# 	def __init__(self):
# 		self.baseurl = 'http://www.budejie.com/'
# 		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) ASD'}
# 		# url队列
# 		self.urlQueue = Queue()
# 		# 响应队列
# 		self.resQueue = Queue()
#
# 	# 生成一个URL队列
# 	def getUrl(self):
# 		for pNum in range(40):
# 			# 拼接URL
# 			url = self.baseurl+str(pNum+1)
# 			self.urlQueue.put(url)
# 	# 响应队列
# 	def getHtml(self):
# 		while True:
# 			url = self.urlQueue.get()
# 			res = requests.get(url,headers = self.headers)
# 			res.encoding = 'utf-8'
# 			html =res.text
# 			# 放入解析队列
# 			self.resQueue.put(html)
# 			# 清除此任务
# 			self.urlQueue.task_done()
# 	# 解析
# 	def getContent(self):
# 		while True:
# 			# 从响应队列中依次获取HTML源码
# 			html = self.resQueue.get()
# 			parseHtml = etree.HTML(html)
# 			r_list = parseHtml.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
# 			for r in r_list:
# 				print(r,'\n')
# 			# 清除任务
# 			self.resQueue.task_done()
#
#
# 	def run(self):
# 		# 存放所有线程
# 		thread_list = []
# 		# 获取URL 队列
# 		self.getUrl()
# 		# 创建getHtml线程
# 		for i in range(5):
# 			threadRes = threading.Thread(target=self.getHtml)
# 			thread_list.append(threadRes)
# 		# 创建解析线程
# 		for j in range(5):
# 			threadParse = threading.Thread(target=self.getContent)
# 			thread_list.append(threadParse)
# 		# 所有线程开始工作
# 		for th in thread_list:
# 			th.setDaemon(True)
# 			th.start()
# 		# 如果队列为空，则执行其他程序
# 		self.urlQueue.join()
# 		self.resQueue.join()
# 		print("运行结束!")
#
# if __name__=='__main__':
# 	begin = time.time()
# 	spider = bsSpider()
# 	spider.run()
# 	end = time.time()
# 	print(end-begin)

# from bs4 import BeautifulSoup
#
# html = '<div id="test">行吧，就这样吧</div>' \
#        '<div id="test">OK</div>' \
#        '<div class="test2">' \
#        '    <span>第二人</span>' \
#        '</div>'
# # 创建解析对象
# soup = BeautifulSoup(html,'lxml')
# # 查找节点
# r_list = soup.find_all(id="test")
# # print(r_list)
# for r in r_list:
# 	print(r.string)

# https://www.cnblogs.com/zhangxinqi/p/9218395.html
# from bs4 import BeautifulSoup
#
# #下面代码示例都是用此文档测试
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# markup="<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup=BeautifulSoup(html_doc,"lxml")
# soup1=BeautifulSoup(markup,"lxml")
# tag=soup.a
# navstr=tag.string
# comment=soup1.b.string
# print(type(tag))   #Tag标签对象
# print(type(comment))   #Comment对象包含文档注释内容
# print(type(navstr))    #NavigableString对象包装字符串内容
# print(type(soup))   #BeautifulSoup对象为文档的全部内容

# <class 'bs4.element.Tag'>
# <class 'bs4.element.Comment'>
# <class 'bs4.element.NavigableString'>
# <class 'bs4.BeautifulSoup'>
# soup=BeautifulSoup(html_doc,'lxml')
# print(soup.head)  #获取head标签
# print(soup.p.b) #获取p节点下的b节点
# print(soup.a.string) #获取a标签下的文本，只获取第一个

# name属性获取节点名称：
# soup.body.name

# soup.p.attrs    #获取p节点所有属性
# soup.p.attrs['class']  #获取p节点class属性
# soup.p['class']  #直接获取p节点class属性
# soup.p.string   #获取第一个p节点下的文本内容
# soup.body.contents   #是直接子节点，不包括子孙节点

# children属性获取的也是节点的直接子节点，只是以生成器的类型返回
# soup.body.children
#
# descendants属性获取子孙节点，返回生成器
# soup.body.descendants
#
# parent属性获取父节点，parents获取祖先节点，返回生成器
# soup.b.parent
# soup.b.parents


start_urls = ['https://app.bilibili.com/x/v2/feed/index?ad_extra='
                  '2F160688A991F9E874393027277D85422F5D26B73238F4'
                  '95719706F7F69C8485FF36E2FDEDDDDA0C080EB4FEFCE5AEC'
                  '82C9AFC0569F4FCF3DD3E33EC93D7E653857B7E4DEAD038A38A'
                  '1042A0ED26DA723A0D0BA60C241B4B54420DA0BE2E10BD3'
                  'A948E2B5F44657D491C165F1FFD9BF24C7914418063E8B8'
                  'B713592526A49376055C964BA80A28D46FF88D87AB0F5FE'
                  '2C3E4576D02086EA1F327FE38DDC1EB8650A8E30FD203A66'
                  'D217191413C40F3D6313F82BAC30DA18FA10925CFF98F850'
                  '4D52E7764D326958134A8B5270E06518355AA427AFDA3C10'
                  'F6F42E5D65D1547C59018A5E54FDD7EB04B36E5BBB22ABC7'
                  'DEB1A4D97BDB3A75DAA2E15C35EFCC3073B3BBADC65A3C1D'
                  'B910ECEA96033B62289966A87C934626F0FD4719724D4F00'
                  '2B05CECCC3F1A62A4CFD2E8F98D6D7A94E9757EFB775A5B841'
                  '9E31BEBB1685CC83E8F6BFDE1EA2626C0A49A5E284D1032B8'
                  '3BE8945161F834A36169B8674D0A5F8A932C3470A0898E42B0'
                  'E91F9EE8CC5E904429FC0F3B890A4205A6150B9D4A1539B9CF8'
                  '183B1A3086E4A562A97300FD4CC1932B46609D98991AF7895DB'
                  '0D2C77F2BD7E9D9271FAF14E6E8DF859A5B4F2C658AD8C61993'
                  '3F20251603AB339B0A7FF72A4E345CEC2E53BE217F46C8C3F5F'
                  '10D8E78A0B27A485C15ECE65E438F0A4EA1429A3635EA04E9C4'
                  '4994212486E019B35208E84F06AF310170F5B6B462BBE1454EA'
                  '520D4A00506AC08B5BC36FC528F804BB64123FCF0CC1382AD77'
                  'ED35896939335A2F0DD1AB395B9F2DC027B80B3B1AB40233EAB'
                  '4B04F1DE16A8B7EF607CE829F8D96D6FF5EF2216D55A81C4581'
                  '2817050E504A3E8EB1862E44A7D72CF1CCAD0FDFE71CC295F30'
                  '6869BC0B6E75AE&appkey=1d8b6e7d45233436&autoplay_car'
                  'd=0&build=5452100&channel=baidu&column=2&device_nam'
                  'e=MI%202A&device_type=0&flush=0&fnval=16&fnver=0&fo'
                  'rce_host=0&fourk=0&idx=0&login_event=1&mobi_app=and'
                  'roid&network=wifi&open_event=cold&platform=android&'
                  'pull=true&qn=32&recsys_mode=0&statistics=%7B%22abte'
                  'st%22%3A%22%22%2C%22platform%22%3A3%2C%22version%22'
                  '%3A%225.45.2%22%2C%22appId%22%3A1%7D&ts=1565310374&'
                  'sign=6998923c0eb6fabc515baa6e4f8d4d9f%20']
print(start_urls[0])


































