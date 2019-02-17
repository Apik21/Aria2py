# -*- coding: utf-8 -*-
import layer as l
from tkinter import Tk, BOTH, Pack
from tkinter import filedialog as fd
from tkinter.ttk import Frame, Button, Style

class Example(Frame):    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Torrent Downloader")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.style = Style()
        self.style.theme_use("alt")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)
 
    def centerWindow(self):
        w = 290
        h = 150
 
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def torrent_check():
    select = fd.askopenfile()
    if select != None:
        print(select.name)
        d1 = l.ariaClass()
        file = select.name #.replace('/','\\')
        d1.torrent_dld(f"{file}")

def magnet_check():
        pass

def main():
    root = Tk()
    root.geometry("300x150+300+300")
    app = Example(root)

    button_T = Button(root, command=torrent_check, text='*.torrent')
    button_M = Button(root, command=magnet_check, text='Magnet')

    button_T.pack()
    button_M.pack()

    root.mainloop()


if __name__ == "__main__":
    main()