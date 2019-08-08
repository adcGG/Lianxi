from bs4 import BeautifulSoup
from urllib import request
import requests
import re
import tkinter


def getHtmldata(url,selectstyle):
	try:
		res = requests.get(url)
		res.raise_for_status()
		soup = BeautifulSoup(res.text, features="html.parser")
		res.close()
		selectanwser = soup.select(selectstyle)
		return selectanwser
	except UnicodeDecodeError as e:
		print('-----UnicodeDecodeError url:', url)
def englishdict(eglsh_word,data):
	part_of_speech = []
	if type(data[0].string) == type(None):
		print('暂无翻译')
	for i in range(len(data)):
		if re.findall('\w+\.',str(data[i].string))!=[]:
			part_of_speech.append(re.findall('\w+\.',data[i].string))
		if str(data[i].string) == 'None':
			return part_of_speech
		if re.findall('\w+\.',str(data[i].string))==[]:
			for j in range(len(part_of_speech)-1,len(part_of_speech)):
				print('2',part_of_speech[j])
				part_of_speech[j].append(str(data[i].string))


# MainForm = tkinter.Tk()
# MainForm.geometry("500x300")
# MainForm.title("电子词典翻译")
# e_show  =  tkinter.Entry(MainForm,width = 24)
# e_show.pack(side="top")
# btn_select = tkinter.Button(MainForm,text='查询',fg = 'black')
# btn_select.pack(side = 'top',pady = '1m')
# btn_select.bind("<Button-1>",)
# Lable_test = tkinter.Label(MainForm,{'title':'这个怎么说'})
# Lable_test.pack(side = 'top',pady = '1m')
# MainForm.mainloop()



# eglsh_word = str(input("输入要查询的单词："))
# url =  'http://www.iciba.com/'+eglsh_word
# CHN_data = 'div ul li span'
# data = getHtmldata(url,CHN_data)
#
#
#
# a = englishdict(eglsh_word,data)
