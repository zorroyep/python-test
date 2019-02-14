# -*- coding:utf-8 -*-



'''
实现界面切换功能
2019-02-12





'''
import tkinter

class BaseDesk():
    def __init__(self,master):
        self.root = master
        self.root.config()
        self.root.title("主窗口")
        self.root.geometry("200x200")

        TelnetFrame(self.root)


class TelnetFrame():
    def __init__(self,master):
        self.master = master
        self.master.config(bg="green")
        self.initface = tkinter.Frame(self.master,)
        self.initface.pack()
        btn = tkinter.Button(self.initface,text='change',command=self.change)
        btn.pack()

    def change(self,):
        self.initface.destroy()
        ConsoleFrame(self.master)

    
class ConsoleFrame():
    def __init__(self,master):
        self.master = master
        self.master.config(bg="blue")
        self.face_1 = tkinter.Frame(self.master,)
        self.face_1.pack()
        btn_back = tkinter.Button(self.face_1,text="face 1 back ",command=self.back)
        btn_back.pack()

    def back(self):
        self.face_1.destroy()
        TelnetFrame(self.master)


if __name__ == "__main__":
    root = tkinter.Tk()
    BaseDesk(root)
    root.mainloop()