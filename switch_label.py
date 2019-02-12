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

        Initface(self.root)


class Initface():
    def __init__(self,master):
        self.master = master
        self.master.config(bg="green")
        self.initface = tkinter.Frame(self.master,)
        self.initface.pack()
        btn = tkinter.Button(self.initface,text='change',command=self.change)
        btn.pack()

    def change(self,):
        self.initface.destroy()
        Face_1(self.master)

    
class Face_1():
    def __init__(self,master):
        self.master = master
        self.master.config(bg="blue")
        self.face_1 = tkinter.Frame(self.master,)
        self.face_1.pack()
        btn_back = tkinter.Button(self.face_1,text="face 1 back ",command=self.back)

    def back(self):
        self.face_1.destroy()
        Initface(self.master)


if __name__ == "__main__":
    root = tkinter.Tk()
    BaseDesk(root)
    root.mainloop()