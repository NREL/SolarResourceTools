#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:55:49 2019

@author: rgupta2
"""

# Importing Libraries

import pandas as pd
import formUI
import componentSel
import calculations
import InstrumentSelection
import utills
#import landingPage as lp
import plotGraph
import datetime as dt
import tkinter, tkinter.filedialog
from tkinter import messagebox
import sys




#if __name__ == '__main__':

######################

# taking file path 

######################

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
    print('Data or List Sheetsare not present')
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

InstrumentList.reset_index(level=0,inplace=True)
InstrumentList.rename(columns={'index':'Instrument'}, inplace=True)

componentList=list(InstrumentList.columns.values)
componentList=componentList[2:]
componentList.remove('Datalogger')
componentList.remove('Responsivity (uv/W/m^2)')
InstrumentSelection.selectInstrument(InstrumentList)

InstrumentValue = int(utills.readList('Instrument')[0])

InstrumentName = InstrumentList['Instrument'][InstrumentValue]

componentSel.component(componentList)
cols = utills.readList('componentList')
comp = pd.DataFrame({'Component':componentList,'Selection':cols},columns= ['Component','Selection'])
componentList = list(comp[comp['Selection']=='1']['Component'])
formData = calculations.gatherFormData(componentList)

uncertainty = calculations.calExpandeduncertainty(componentList, InstrumentList, InstrumentName)
uncertainty = calculations.calStandardUncert(formData, uncertainty)

report = calculations.calculateuncertainty(InstrumentName, data, InstrumentList, formData, uncertainty)

uncertPercent = calculations.finalUncertPercentage(report,InstrumentName)

######################
    
# Writing Excel file

######################

name= 'output' +str(dt.datetime.now())
writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
uncertPercent.to_excel(writer, sheet_name= 'Final Uncertainty')
uncertainty.to_excel(writer, sheet_name= 'Exp & Std Uncert')
formData.to_excel(writer, sheet_name= 'Selected components')
report.to_excel(writer, sheet_name= 'Final Calculation')
#plotGraph.plot(report, componentList, InstrumentName)
#plotGraph.plotUncertainty(report, InstrumentName)
writer.save()
formUI.thankYou()
sys.exit()