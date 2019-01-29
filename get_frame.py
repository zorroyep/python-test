# -*- coding:utf-8 -*-

import tkinter

root = tkinter.Tk()

'''
for multicolor in ['red','blue','yellow','green','white','black']:
    tkinter.Frame(height=20,width=100,bg=multicolor).pack()
'''


'''
fm = []
for color in ['red','blue']:
    #注意这个创建Frame的方法与其它创建控制的方法不同，第一个参数不是root
    fm.append(tkinter.Frame(height=200,width=400,bg=color))
#向下面的Frame中添加一个Label
tkinter.Label(fm[1],text="hello label").pack()
#注意这里我们先pack了子控件，再pack了父控件。
#如果父控件没有被pack，子控件是不会显示的。
fm[0].pack()
fm[1].pack()
'''


def Console():
    pass

def getTelnet():
    pass


#菜单
menubar = tkinter.Menu(root)
for each in ['文件','视图','编辑','关于']:
    menubar.add_command(label=each)
root['menu'] = menubar

#使用ttk控件
from tkinter import ttk

#增加console和telnet界面

class Application(tkinter.Frame):
    def say_hi(self):
        print('hi,everyone.')

    def createWidgets(self):
        self.QUIT = tkinter.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side":"left"})

        self.hi_there = tkinter.Button(self)
        self.hi_there["text"] = "Hello"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side":"left"})

    def __init__(self,master=None):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()



app = Application(master=root)
app.mainloop()
root.destroy()