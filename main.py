# -*- coding: utf-8 -*-
import layer as l
from tkinter import *
from tkinter import filedialog as fd


def torrent_check():
    select = fd.askopenfile()
    if select != None:
        print(select.name)


root = Tk()

#d1 = l.ariaClass()
#d1.torrent_dld('./123.torrent')
if __name__ == "__main__":
    button = Button(root, command=torrent_check, text='*.torrent')
    button.pack()
    root.mainloop()