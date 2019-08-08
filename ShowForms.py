import tkinter
MainForm = tkinter.Tk()
MainForm.geometry("800x600")
MainForm.title('曾智能创造的窗口')
MainForm['background'] = 'LightSlateGray'
btn1 = tkinter.Button(MainForm,text = '退出',fg = 'black') #在窗体上创建btn1按钮
btn1.pack() # pack（）方法将btn1按钮放在窗体上
def turn_property(event):
	event.widget["activeforeground"] = "red" # 鼠标左键按下时，标题显示红色
	event.widget["text"] = "OK" # 鼠标指针接触按钮时，标题变OK
btn1.bind("<Enter>",turn_property)
MainForm.mainloop()