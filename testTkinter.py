# -*- coding:utf-8 -*-

import tkinter

root = tkinter.Tk()

#建立一个主界面类
#
class Application(tkinter.Frame):
    def chg_telnet(self):
        if self.frame_2:
            self.frame_2.destroy()
        elif self.frame_1:
            self.frame_1.pack()
        else:
            self.frame_1 = TelnetInterface(self)
            self.frame_1.pack()

        

    def chg_console(self):
        if self.frame_1:
            self.frame_1.destroy()
        elif self.frame_2:
            #self.frame_2 = ConsoleInterface(self)
            self.frame_2.pack()
        else:
            self.frame_2 = ConsoleInterface(self)
            self.frame_2.pack()
        


    def __init__(self,master):
        super().__init__()
        self.pack()
        self.telnet_btn = tkinter.Button(self,text="Telnet",command=lambda:self.chg_telnet())

        self.telnet_btn.pack()
        self.console_btn = tkinter.Button(self,text="串口",command=lambda:self.chg_console())
        self.console_btn.pack()

        self.mainface = tkinter.Label(self,text="欢迎使用！")
        self.mainface.pack()

        self.frame_1 = TelnetInterface(self)
        self.frame_2 = ConsoleInterface(self)


#telnet界面类
class TelnetInterface(tkinter.Frame):
    def __init__(self,parent):
        super().__init__()
        self.ip_address = tkinter.Label(self,text="IP地址")
        self.ip_address.pack()
        self.telnet_text = tkinter.Label(self,text="我是telnet界面")
        self.telnet_text.pack()





#console界面类
class ConsoleInterface(tkinter.Frame):
    def __init__(self,parent):
        super().__init__()
        self.console_port = tkinter.Label(self,text="COM口")
        self.console_port.pack()
        self.console_text = tkinter.Label(self,text="我是Console界面")
        self.console_text.pack()



base = Application(root)
print(base.winfo_toplevel())
print(base.__dict__)
base.mainloop()