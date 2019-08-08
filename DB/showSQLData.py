def turn_property(event):
	getSQLData()
def getSQLData():
	import pymysql
	import sys
	try:
		conn = pymysql.connect(host='localhost', user='root', passwd='979818137zzn', db='gkdb', port=3306,
		                       charset='utf8')
	except:
		print("打开数据库连接出错，请检查！")
		conn.close()
		sys.exit()
	cur = conn.cursor()
	selectSQL = 'Select * from t_fish'
	cur.execute(selectSQL)
	for row in cur.fetchall():
		tree.insert("",0,text = row[0],values = (row[1],row[2],row[3],row[4]))
from tkinter import ttk
import tkinter as tk
root = tk.Tk()
tree  =ttk.Treeview(root)
tree["columns"] = ("name","nums","price","Explain")
tree.column("name",width = 50)
tree.column("nums",width = 50)
tree.column("price",width = 50)
tree.column("Explain",width = 50)
tree.heading("name",text = "名称")
tree.heading("nums",text = "数量")
tree.heading("price",text = "单价（元）")
tree.heading("Explain",text = "说明")
tree.pack(side = "top")
bs = tk.Button(root,text = "显示数据",width = 10)
bs.bind("<Button-1>",turn_property)
bs.pack(side = "top")
root.mainloop()


