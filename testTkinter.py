# -*- coding:utf-8 -*-

import tkinter

root = tkinter.Tk()

#建立一个frame类
#
class Application(tkinter.Frame):
    def chg_telnet(self):
        pass

    def chg_console(self):
        pass

    def __init__(self):
        super.__init__()
        self.mainFrame = tkinter.Frame()
        self.telnet_btn = tkinter.Button()
root.mainloop()