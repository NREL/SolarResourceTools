#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:55:09 2019

@author: rgupta2
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import sys
import signal, os


def loadFile():
        
    def upload():

            f=open('filePath','w+')
            f.write(str(root.filename))
            f.close()
            root.after(1, root.withdraw())
            f=open('filePath', 'r')
            temp = f.read()
            f.close()
            if len(temp) <1:
                if (len(root.filename)<1):
                       messagebox.showerror("Error", "File not provided")
                       sys.exit()
            #print (root.filename)
            
    root = Tk()
    root.title('uncertainty Evaluator')
    root.wm_geometry('300x170+100+100')
    Label(root, text="Please upload the Excel file ", justify = CENTER, padx = 20, pady=40).pack()

    root.filename =  filedialog.askopenfilename(initialdir = "/", title = "Select file")
    #print (root.filename)
    Button(root, text ="Upload", command = upload, pady =10).pack()
    root.mainloop()