#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:55:49 2019

@author: rgupta2
"""

# Importing Libraries

import pandas as pd
import formUI
import ComponentSel
import calculations
import InstrumentSelection
import utills
#import landingPage as lp
import plotGraph
import time
import tkinter, tkinter.filedialog
from tkinter import messagebox
import sys
import os



#if __name__ == '__main__':

######################

# taking file path 

######################
sys.setrecursionlimit(1500)
root = tkinter.Tk()
root.withdraw()
path = tkinter.filedialog.askopenfilename(parent=root,initialdir="/",title='Upload Excel file',filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
if (len(path) <1):
    messagebox.showerror("Error", "File not provided. Please Try Again.")
    sys.exit()
    
######################
    
# Importing file

######################
    
try:
    data= pd.read_excel(path, sheet_name='Data', skiprows=None)
    InstrumentList= pd.read_excel(path, sheet_name='List', skiprows=None, index=0)
except:
    messagebox.showerror("Error", 'Data or List Sheet not present.')
    print('Data or List Sheet not present')
    sys.exit()
root.after(1,root.destroy())

# taking file using Console
'''
#fileName='radiometer_uncert_tool_11022017.xlsx'
fileName='radiometer_uncert.xlsx' # along with the extention 
path='~/Desktop/Projects/uncertainty/'
data= pd.read_excel(path+fileName, sheet_name='Data', skiprows=1)
InstrumentList= pd.read_excel(path + fileName, sheet_name='List', skiprows=None, index=0)
'''
######################
    
# Calculations

######################

#InstrumentList.reset_index(level=0,inplace=True)
InstrumentList.rename(columns={'Unnamed: 0':'Instrument'}, inplace=True)

ComponentList=list(InstrumentList.columns.values)
ComponentList=ComponentList[2:]
ComponentList.remove('Datalogger')
ComponentList.remove('Responsivity (uv/W/m^2)')
InstrumentSelection.selectInstrument(InstrumentList)

InstrumentValue = int(utills.readList('Instrument')[0])

InstrumentName = InstrumentList['Instrument'][InstrumentValue]

ComponentSel.Component(ComponentList)
cols = utills.readList('ComponentList')
comp = pd.DataFrame({'Component':ComponentList,'selection':cols},columns= ['Component','selection'])
ComponentList = list(comp[comp['selection']=='1']['Component'])
formData = calculations.gatherFormData(ComponentList)

uncertainty = calculations.calExpandeduncertainty(ComponentList, InstrumentList, InstrumentName)
uncertainty = calculations.calStandardUncert(formData, uncertainty)

report = calculations.calculateuncertainty(InstrumentName, data, InstrumentList, formData, uncertainty)

uncertPercent = calculations.finalUncertPercentage(report,InstrumentName)



######################
    
# Writing Excel file

######################

name= 'output' + str(time.time()).replace('.','-')

writer = pd.ExcelWriter(name + '.xlsx', engine='xlsxwriter')
uncertPercent.to_excel(writer, sheet_name= 'Final uncertainty')
uncertainty.to_excel(writer, sheet_name= 'Exp & Std Uncert')
formData.to_excel(writer, sheet_name= 'Selected Components')
report.to_excel(writer, sheet_name= 'Final calculation')
writer.save()
os.remove('ComponentList')
os.remove('Instrument')
os.remove('temp')
plotGraph.plot(report, ComponentList,InstrumentName)
plotGraph.plotUncertainty(report, InstrumentName)
formUI.thankYou()
sys.exit()