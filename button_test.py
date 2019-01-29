# -*- coding:utf-8 -*-

import tkinter
RELIEFS = [tkinter.SUNKEN,tkinter.RAISED,tkinter.GROOVE,tkinter.RIDGE,tkinter.FLAT]

class ButtonsApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.img = tkinter.PhotoImage(file="python.gif")
        self.btn = tkinter.Button(self,text="Button with image",
                                    image=self.img,compound=tkinter.LEFT,
                                    command=self.disable_btn)

        self.btns = [self.create_btn(r) for r in RELIEFS]
        self.btn.pack()
        for btn in self.btns:
            btn.pack(padx=10,pady=10,side=tkinter.LEFT)

    def create_btn(self,relief):
        return tkinter.Button(self,text=relief,relief=relief)
    
    def disable_btn(self):
        self.btn.config(state=tkinter.DISABLED)


if __name__ == "__main__":
    app = ButtonsApp()
    app.mainloop()