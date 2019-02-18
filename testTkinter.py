# -*- coding:utf-8 -*-

import tkinter

root = tkinter.Tk()

#建立一个主界面类
#
class Application(tkinter.Frame):
    def chg_telnet(self):
        self.telnet_inter = TelnetInterface(self)
        self.telnet_inter.pack()
        self.telnet_text = tkinter.Label(text="我是telnet界面")
        self.telnet_text.pack()

    def chg_console(self):
        self.console_inter = ConsoleInterface(self)
        self.console_inter.pack()
        self.telnet_text = tkinter.Label(text="我是Console界面")
        self.telnet_text.pack()


    def __init__(self,master):
        super().__init__()
        self.pack()
        self.telnet_btn = tkinter.Button(self,text="Telnet",command=self.chg_telnet)

        self.telnet_btn.pack()
        self.console_btn = tkinter.Button(self,text="串口",command=self.chg_console)
        self.console_btn.pack()

        self.mainface = tkinter.Label(self,text="欢迎使用！")
        self.mainface.pack()


#telnet界面类
class TelnetInterface(tkinter.Frame):
    def __init__(self,parent):
        super().__init__()
        self.ip_address = tkinter.Label(self,text="IP地址")
        self.ip_address.pack()





#console界面类
class ConsoleInterface(tkinter.Frame):
    def __init__(self,parent):
        super().__init__()
        self.console_port = tkinter.Label(self,text="COM口")
        self.console_port.pack()



base = Application(root)
print(base.winfo_toplevel())
base.mainloop()