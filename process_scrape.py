import requests
import multiprocessing
from requests.exceptions import ConnectionError
import os

def scrape(url):
	try:
		r = requests.get(url)

		print("爬取%s成功！收到%s"%(url,requests.get(url)))
		filelocal = os.getcwd() + '\process_scrape.txt'
		txt = r.text + '\n\n\n\n\n#######################################################'
		openfile = open(filelocal,'a')
		openfile.write(txt)
		openfile.close()
		print("往文件里写内容成功！")
	except ConnectionError:
		print("爬取%s出错！"%(url))

if __name__=="__main__":
	pool = multiprocessing.Pool()
	urls = [
		'http://www.metro.cn/',
		# 'http://www.shuichan.cc/',
		# 'http://www.51sole.com/',
		# 'http://www.x009.com/',
		# 'http://www.x009.comd/'
	]
	pool.map(scrape,urls)
