# -*- coding:utf-8 -*-

import tkinter
#import sys


#建立一个主界面类
#
class Application(tkinter.Frame):
    def chg_telnet(self):
        print("开始执行chg_telnet")
        if self.frame_2.winfo_exists():
            self.frame_2.destroy()
            #print(sys.getrefcount(self.frame_2))
            print("开始判断1")
            #self.frame_1 = TelnetInterface(self)
            #self.frame_1.pack()
        if self.frame_1.winfo_exists():
            print("开始判断2")
            #self.frame_1.destroy()
            self.frame_1.grid(row=2,column=0,pay=3)
        else:
            print("开始判断3")
            self.frame_1 = TelnetInterface(self)
            self.frame_1.grid(row=2,column=0,pady=3)

        

    def chg_console(self):
        print("开始执行console_telnet")
        if self.frame_1.winfo_exists():
            print("开始判断1")
            self.frame_1.destroy()
        if self.frame_2.winfo_exists():
            print("开始判断2")
            #self.frame_2.destroy()
            self.frame_2.grid(row=2,column=0,pady=3)
        else:
            print("开始判断3")
            self.frame_2 = ConsoleInterface(self)
            self.frame_2.grid(row=2,column=0,pady=3)
        


    def __init__(self,master):
        super().__init__()
        self.grid()
        
        #两个切换界面的按钮，分别占第一行第一列和第一行第二列（从0开始计算）。
        self.telnet_btn = tkinter.Button(self,text="Telnet",width=10,command=lambda:self.chg_telnet())
        self.telnet_btn.grid(row=0,column=0,padx=1,pady=3,)
        self.console_btn = tkinter.Button(self,text="串口",width=10,command=lambda:self.chg_console())
        self.console_btn.grid(row=0,column=3,padx=1,pady=3)

        #self.mainface = tkinter.Label(self,text="欢迎使用！")
        #self.mainface.pack()

        self.frame_1 = TelnetInterface(self)
        self.frame_1.grid(row=2,column=0,pady=3)
        self.frame_2 = ConsoleInterface(self)
        
        #self.destroy()

        


#telnet界面类
class TelnetInterface(tkinter.Frame):
    def __init__(self,parent):
        super().__init__()
        self.telnet_text = tkinter.Label(self,text="我是telnet界面")
        self.telnet_text.grid(row=3,column=0,)
        self.ip_address = tkinter.Label(self,text="IP地址")
        self.ip_address.grid(row=4,column=0,)
        #IP地址输入栏
        #打印回显栏
        #添加一些按钮
        





#console界面类
class ConsoleInterface(tkinter.Frame):
    def __init__(self,parent):
        super().__init__()
        self.console_text = tkinter.Label(self,text="我是Console界面")
        self.console_text.grid(row=3,column=0,)
        self.console_port = tkinter.Label(self,text="COM口")
        self.console_port.grid(row=4,column=0,)
        #连接串口所需要的参数
        #1，串口波特率，端口号，数据位，校验，停止位，流控

        #2，还没有想好，在配置串口时，是用对话框的形式还是直接在软件界面上配置的形式
        



root = tkinter.Tk()
root.title("串口小工具 v1.0")
root.geometry("500x400")
baseDesk = Application(root)
print(baseDesk.winfo_toplevel())
#print(dir(baseDesk))
baseDesk.mainloop()