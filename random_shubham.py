from Tkinter import *
import urllib2
import tkFileDialog
import os
import Tkinter as tk




root=Tk()
root.title("PACKAGE DOWNLOADER")
root.geometry('700x200')
url1=tk.StringVar()
var = IntVar()
titleLabel=tk.Label(root,text="Packege Downloading prompt")
titleLabel.grid(row=1,column=1)
urlLabel=tk.Label(root,text="PACKAGE NAME")
urlLabel.grid(row=2,column=5)
urlentry=tk.Entry(root,textvariable=url1,bg='lightblue', fg='black')
urlentry.grid(row=2,column=10)
status=tk.StringVar()

titleLabe2=tk.Label(root,text="STATUS")
titleLabe2.grid(row=5,column=5)
titleLabe3=tk.Label(root,textvariable=status,bg='lightblue',width=10)
titleLabe3.grid(row=5,column=10)

def connectcmd():
    os.system('pip install '+url1.get())
    status.set("DONE")

def connectcmd1():
    os.system('easy_install ' + url1.get())
    status.set("DONE")

def connectcmd2():
    os.system('pip install ' + url1.get())
    status.set("DONE")
def connectcmd4():
    fileName=tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes=(("whlfiles",".whl"),("all files","*.*")))
    print fileName
    url1.set(fileName)
submitButton1 = tk.Button(root, text="BROWSE FILE",height=1, command=connectcmd4)
submitButton1.grid(row=2, column=30)
submitButton=tk.Button(root,text="PIP",width=30,command=connectcmd)
submitButton.grid(row=50,column=30)
submitButton2=tk.Button(root,text="EASY_INSTALL",width=30,command=connectcmd1)
submitButton2.grid(row=60,column=30)
submitButton3=tk.Button(root,text="WHL INSTALL(BROWSE TO GIVE PATH)",command=connectcmd2)
submitButton3.grid(row=70,column=30)
root.mainloop()
