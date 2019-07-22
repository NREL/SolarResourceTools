#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:36:23 2019

@author: rgupta2
"""

import tkinter
import os, sys

def thankYou():
    
    def close():
        root.after(1, root.withdraw())
        root.after(1, root.destroy())
        sys.exit()
        
    root=tkinter.Tk()
    root.title("Finish!!")
    root.wm_geometry("330x260+100+100")
    location = os.getcwd()
    tkinter.Label(root, text="Thank you! \n\n\n output file has been created at : \n\n "+location, justify = tkinter.CENTER, padx = 20, pady=40).pack()
    tkinter.Button(root, text ="Close", command = close, pady =10).pack()
    root.mainloop()



def takeParams(param):
    def rootDest():
        #root.destroy()
        root.after(1, root.destroy())
    
    def hitSubmit():
        f=open('temp','w+')
        f.write(ip.get()+'\n')
        f.write(uncert.get()+'\n')
        f.write(dist.get()+'\n')
        f.write(sym.get()+'\n')
        f.write(analysis.get()+'\n')
        f.close()
        root.after(1, root.destroy())
        
    
    root=tkinter.Tk()
    root.title("Component  Configuration")
    root.wm_geometry("580x280+100+100")

    # Create a Component variables
    ip = tkinter.StringVar(root)
    uncert = tkinter.StringVar(root) 
    dist = tkinter.StringVar(root)
    sym = tkinter.StringVar(root)
    analysis = tkinter.StringVar(root)


    # Dictionary with options
    inputVars = { 'S','V','E'}
    ip.set('S') # set the default option
    uncertaintyType = { 'Relative','Absolute'}
    uncert.set('Relative') # set the default option
    distribution ={ 'Rectangular','Normal', 'Triangular', 'U-shaped'}
    dist.set('Rectangular') # set the default option
    symmetry = {'Symmetric', 'One-Sided'}
    sym.set('Symmetric') # set the default option
    incAnalysis = {'Yes', 'No'}
    analysis.set('Yes') # set the default option
    j=3

# Designing UI of form
    tkinter.Label(root, text="  ",justify=tkinter.LEFT).grid(row = 0, column = 2)
    tkinter.Label(root, text="   Please select configuration for "+ param).grid(row = 1, column = 2)
    tkinter.Label(root, text="  ",justify=tkinter.LEFT).grid(row = 2, column = 2)
    #tkinter.Label(root, text=param).grid(row = j, column = 1)
    tkinter.Label(root, text="Select Input type").grid(row = j, column = 2)
    
    menu1 = tkinter.OptionMenu(root, ip, *inputVars)
    menu1.config(width=10)
    menu1.grid(row = j, column =4)
    
    tkinter.Label(root, text="Uncertainty Type",justify=tkinter.LEFT).grid(row = j+1, column = 2)
    menu2= tkinter.OptionMenu(root, uncert, *uncertaintyType)
    menu2.config(width=10)
    menu2.grid(row = j+1, column = 4)
    
    tkinter.Label(root, text="Distribution Type",justify=tkinter.LEFT).grid(row = j+2, column = 2)
    menu3= tkinter.OptionMenu(root, dist, *distribution)
    menu3.config(width=10)
    menu3.grid(row = j+2, column = 4)
    
    tkinter.Label(root, text="Symmetry Type",justify=tkinter.LEFT).grid(row = j+3, column = 2)
    menu4= tkinter.OptionMenu(root, sym, *symmetry)
    menu4.config(width=10)
    menu4.grid(row = j+3, column = 4)
    
    tkinter.Label(root, text="Include in Analysis",justify=tkinter.LEFT).grid(row = j+4, column = 2)
    menu5= tkinter.OptionMenu(root, analysis, *incAnalysis)
    menu5.config(width=10)
    menu5.grid(row = j+4, column = 4)
    
    tkinter.Label(root, text="  ").grid(row = j+5, column = 2)
    submitButton = tkinter.Button(root, text = "Submit", command = hitSubmit)
    submitButton.grid(row = 9, column = 4)
    submitButton.config(width=10)
    submitButton.configure(background = 'grey')
    root.mainloop()
    
#takeParams("ws")

'''
from tkinter import *
import tkinter
def scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=650,height=330)
listCols=['sd', 'wd']
root=Tk()
root.title("Component Selection")
root.wm_geometry("720x350+100+100")

myframe=Frame(root,relief=GROOVE,width=10,height=100,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",scroll)

# Create a Component variables
ip = tkinter.StringVar(root)
uncert = tkinter.StringVar(root) 
dist = tkinter.StringVar(root)
sym = tkinter.StringVar(root)
analysis = tkinter.StringVar(root)


# Dictionary with options
inputVars = { 'E','V','S'}
ip.set('Select Option') # set the default option
uncertaintyType = { 'Relative','Absolute'}
uncert.set('Select Option') # set the default option
distribution ={'Normal', 'Rectangular', 'Triangular', 'U-shaped'}
dist.set('Select Option') # set the default option
symmetry = {'Symmetric', 'One-Sided'}
sym.set('Select Option') # set the default option
incAnalysis = {'Yes', 'No'}
analysis.set('Select Option') # set the default option

# Designing UI of form
j=3
for i in listCols:
    tkinter.Label(frame, text="  ").grid(row = 0, column = 2)
    tkinter.Label(frame, text="Please tell us what you want").grid(row = 1, column = 2)
    tkinter.Label(frame, text="  ").grid(row = 2, column = 2)
    tkinter.Label(frame, text=i).grid(row = j, column = 1)
    tkinter.Label(frame, text="Select Input type").grid(row = j, column = 2)
    menu1 = tkinter.OptionMenu(frame, ip, *inputVars).grid(row = j, column =4)
    tkinter.Label(frame, text="uncertainty Type").grid(row = j+1, column = 2)
    menu2= tkinter.OptionMenu(frame, uncert, *uncertaintyType).grid(row = j+1, column = 4)
    tkinter.Label(frame, text="Distribution Type").grid(row = j+2, column = 2)
    menu3= tkinter.OptionMenu(frame, dist, *distribution).grid(row = j+2, column = 4)        
    tkinter.Label(frame, text="Symmetry Type").grid(row = j+3, column = 2)
    menu4= tkinter.OptionMenu(frame, sym, *symmetry).grid(row = j+3, column = 4)        
    tkinter.Label(frame, text="Include in Analysis").grid(row = j+4, column = 2)
    menu5= tkinter.OptionMenu(frame, analysis, *incAnalysis).grid(row = j+4, column = 4)        
    tkinter.Label(frame, text="  ").grid(row = j+5, column = 2)
    j=j+6

def hitSubmit():
    choices={}
    choices[ip] = ip.get()
    return choices

submitButton = Button(frame, text = "Submit", command = hitSubmit).grid(row = j+1, column = 2)


root.mainloop()
root.withdraw()
'''