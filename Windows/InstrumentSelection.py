#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:37:39 2019

@author: rgupta2
"""

import tkinter
import signal

def selectInstrument(dList):
    def scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=360,height=410)
    
    def hitNext():
        f=open('Instrument','w+')
        f.write(str(value.get()))
        f.close()
        root.after(100,root.destroy())

    root =tkinter.Tk()
    root.title("Instrument Selection")
    root.wm_geometry('400x480+100+100')
    
    myframe=tkinter.Frame(root,relief=tkinter.GROOVE,width=10,height=100,bd=1)
    myframe.place(x=10,y=50)
    
    canvas=tkinter.Canvas(myframe)
    frame=tkinter.Frame(canvas)
    myscrollbar=tkinter.Scrollbar(myframe,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",scroll)
    
    value = tkinter.IntVar()
    
    tkinter.Label(root, text="""Choose a Instrument""", justify = tkinter.LEFT).pack()
    for i in range(len(dList['Instrument'])):
        tkinter.Radiobutton(frame, text=dList['Instrument'][i], padx = 25,pady=1, variable=value, value=i).pack(anchor=tkinter.W)

    nextButton=tkinter.Button(frame, text = 'Next', command = hitNext)
    nextButton.pack(anchor=tkinter.W, side=tkinter.RIGHT)
    root.mainloop()
    
#selectInstrument(dList)