import tkinter
MainForm = tkinter.Tk()
MainForm.geometry("250x150")
btn1 = tkinter.Button(MainForm,text = "1",fg = "black")
btn2 = tkinter.Button(MainForm,text = "2",fg = "black")
btn3 = tkinter.Button(MainForm,text = "3",fg = "black")

# btn1.pack(side = "top")
# btn2.pack(side = "top")
# btn3.pack(side = "top")


btn1.pack(side = "left",padx = "1m")
btn2.pack(side = "left",padx = "1m")
btn3.pack(side = "left",padx = "1m")


text = tkinter.Text(MainForm,bg = "black",fg = 'blue')
text.pack(side = "left",padx = "1m")
textlist = ''

def func(event):
	if event.keycode != 229:
		# print('key:',event.char)
		# print("x:",event.x,"y:",event.y)
		print(event)
		global textlist
		textlist = textlist+event.char
		print(textlist)

def func2(event):
	print(textlist)

text.bind("<Key>",func)
text.bind("<FocusOut>",func2)


MainForm.mainloop()