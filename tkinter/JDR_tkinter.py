import tkinter
from tkinter import *

window = Tk()


class Test:
    list = []
    string = tkinter.StringVar()

    def pushToList(self, value):
        self.list.append(value)

    def listString(self):
        string = ""
        for i in self.list:
            string += f'{i}, '

        self.string.set(string)

        return string


t = Test()


def push():
    t.pushToList("ok")


label = Label(textvariable=t.string)
label.pack()

button = Button(window, text="Push", command=push)
button.pack()

window.mainloop()
