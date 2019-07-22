#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:43:01 2019

@author: rgupta2
"""

import tkinter
import datetime
import signal,os

def Component(ComponentList):

    def scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=280,height=460)

    def hitNext():
        f=open('ComponentList','w+')
        for i in temp:
            f.write(str(i.get())+'\n')
        f.close()
        root.after(100,root.destroy())

    root =tkinter.Tk()
    root.title("Component Selection")
    root.wm_geometry('325x430+100+100')
    
    myframe=tkinter.Frame(root,relief=tkinter.GROOVE,width=10,height=80,bd=1)
    myframe.place(x=10,y=100)
    
    canvas=tkinter.Canvas(myframe)
    frame=tkinter.Frame(canvas)
    myscrollbar=tkinter.Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",scroll)
    
    lab=tkinter.Label(root, text= ' ')
    lab.grid(row=0, column=2)
    
    lab=tkinter.Label(root, text= 'Please uncheck the unwanted components\n\nNote: If Zenith and Azimuth response are checked then\n uncheck Directional response and vice versa.')
    lab.grid(row=1, column=2)
    temp=[]
    j=3
    for i in ComponentList:
        caption = i
        i = tkinter.IntVar(root)
        var=datetime.datetime.now()
        temp.append(i)
        var=tkinter.Checkbutton(frame,text=caption, variable=i)
        var.grid(row=j+2,column=1)
        var.config(justify= tkinter.LEFT)
        var.select()
        j=j+1
    nextButton=tkinter.Button(frame, text = 'Next', command = hitNext)
    nextButton.grid(row = j+3, column = 1)
    root.mainloop()