# P210-212
from tkinter import *
master = Tk()
master.geometry("700x600")
#=========================================================Label标签组件
l_show = Label(master,text = "曾智能")
photo = PhotoImage(file = "201506211831476696.gif")
l_show1 = Label(master,image = photo)
l_show.pack(side = "left")
l_show1.pack(side = "left")
#=========================================================Entry单行文本组件
e_show = Entry(master,width = 10)
e_show.pack(side = "left")
#=========================================================Text多行文本组件
t_show = Text(master,width =10,height = 4)
t_show.pack(side = "bottom")
#=========================================================Checkbutton复选框组件
var  = StringVar()
c_show = Checkbutton(master,text = "蓝猫",variable = var, onvalue  = "RGB",offvalue = "L",fg = "blue")
c_show.pack(side = "top")
#=========================================================Radiobutton单选组件
v = IntVar()
r_show = Radiobutton(master,text = "One",variable = v,value = 1)
r_show.pack(anchor = W)
#=========================================================frame框架组件
f_show = Frame(master,height = 200,width = 200,bd = 1,bg = "white",relief = SUNKEN)
f_show.pack(anchor = "center")
#=========================================================LabelFrame标签框架组件
lf_show = LabelFrame(master,text = "Group",padx = 5,pady = 5)
lf_show.pack(padx = 10 , pady = 10,expand = "yes")
e1 = Entry(lf_show,width = 10)
e1.pack()
e2 = Entry(lf_show,width = 10)
e2.pack()
#=========================================================Listbox列表框组件
lb_show = Listbox(master,bg = "yellow",height = 5,width = 20)
lb_show.pack(side = "top")
for item in ["one","two","three","four"]:
	lb_show.insert(END,item)
#=========================================================Scrollbar滚动条组件
s_show = Scrollbar(master)
s_show.pack(side = RIGHT,fill = Y)
lb_show1 = Listbox(master,fg = "red",height = 5,width = 20)
lb_show1['yscrollcommand'] = s_show.set
lb_show1.pack(side = "right")
for item in ["1","2","3","4","5","6","7"]:
	lb_show1.insert(END,item)
s_show.config(command = lb_show.yview)
#=========================================================Scale刻度条组件
sc_show = Scale(master,from_=0,to =100)
sc_show.pack(side = "right")
#=========================================================Message及Button组件
def showMessage(event):
	m1 = Message(master,text = "确认",fg = "black")
	m1.pack()
b_show=Button(master,text = "确认",fg = "black")
b_show.bind("<Button-1>",showMessage)
b_show.pack(side = "left")
#=========================================================Spingbox组件
sb_show = Spinbox(master,from_ = 0,fg="black")
sb_show.pack(side = "left")
#=========================================================Toplevel子窗体组件
tL_show = Toplevel(master)
tL_show.wm_attributes("-topmost",1)
tL_show.title("OK!")
t1_show = Text(tL_show,width =10,height = 4)
t2_show = Text(tL_show,width = 10,height = 4)
t1_show.pack()
t2_show.pack()
#========================================================PanedWindow组件
pw = PanedWindow(orient = VERTICAL,bg = "green")
pw.pack(fill = BOTH,expand=1)
for w in [Label,Button,Checkbutton,Radiobutton]:
	pw.add(w(pw,text = "可上下移动"))

mainloop()


