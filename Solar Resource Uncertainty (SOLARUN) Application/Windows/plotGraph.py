#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:04:51 2019

@author: rgupta2
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.dates as md
import pandas as pd
import sys
import tkinter
from tkinter import messagebox


def plot(report, componentList, InstrumentName):
    startPoint = (report.shape[1])-len(componentList)
    stopPoint = startPoint + len(componentList)-1
    graphData = report.iloc[:, startPoint:stopPoint]

    x=report[InstrumentName]
    for component in graphData.columns:
        print(component)
        y=report[component]
        plt.scatter(x,y)
        plt.legend(loc = 'center left', bbox_to_anchor=(1,0.5))
    plt.xlabel('Irradiance W/m2')
    plt.ylabel('Contribution to Uncertainty %')
    plt.title('Irradiation vs. Uncertainty Contribution')
    plt.ylim(0,30)
    plt.grid(True)
    plt.savefig('Graph.png', bbox_inches ='tight')
    plt.show()
   
#plot(report, componentList, InstrumentName)
def lam(dates):
    return dates.date()

def plotUncertainty1(report, InstrumentName):
    firstDate = report.iloc[0,0]#report[0:1]['DATE'][0]
    DateCol = report.columns[0]
    TimeCol = report.columns[1]
    temp = report[report[DateCol]==firstDate]
    temp['xlab'] = temp[TimeCol].apply(lam)
    x = (temp[TimeCol].map(str))
    y=temp[InstrumentName]
    yerr = temp['ExpUncert Wm^-2']
    plt.errorbar(x.values,y, yerr, errorevery=1, ecolor ='red',color='green')
    plt.tick_params(axis='x', labelrotation=90)
    plt.xlabel('Time')
    myfmt=md.DateFormatter('%H')
    plt.xaxis.set_major_formatter(myfmt)
    plt.ylabel('Irradiance W/m^2')
    green_patch = mpatches.Patch(color='green', label='Irradiance in W/m^2')
    red_patch = mpatches.Patch(color='red', label='Expanded uncertainty values at 95% conf. level')

    plt.legend(loc = 2,handles=[green_patch,red_patch],bbox_to_anchor=(0,1))
    plt.grid(True)
    plt.ylim(0,1400)
    #plt.xlim(6,19)
    plt.savefig('Graph2.png', bbox_inches ='tight',dpi =500)
    plt.show()


def plotUncertainty(report, InstrumentName):

    firstDate = report.iloc[0,0]#report[0:1]['DATE'][0]
    DateCol = report.columns[0]
    TimeCol = report.columns[1]
    temp = report[report[DateCol]==firstDate]
    try:
        temp[DateCol].apply(lam)
    except:
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("Error", 'Date column in excel should be in Date format')
        print('Date column in excel should be in Date format')
        sys.exit()
        root.after(1,root.destroy())

    temp[TimeCol] = pd.to_datetime(temp[DateCol].map(str) +" " + temp[TimeCol].map(str))

    x = (temp[TimeCol])
    y=temp[InstrumentName]
    yerr = temp['ExpUncert Wm^-2']

    fig, ax = plt.subplots()
    ax.errorbar(x.values,y, yerr, errorevery=1, ecolor ='red',color='green')
    myfmt=md.DateFormatter('%H')
    ax.xaxis.set_major_formatter(myfmt)
    plt.xlabel('Time')
    myfmt=md.DateFormatter('%H')
    #plt.xaxis.set_major_formatter(myfmt)
    plt.ylabel('Irradiance W/m^2')
    green_patch = mpatches.Patch(color='green', label='Irradiance in W/m^2')
    red_patch = mpatches.Patch(color='red', label='Expanded uncertainty values at 95% conf. level')

    plt.legend(loc = 2,handles=[green_patch,red_patch],bbox_to_anchor=(0,1))
    plt.grid(True)
    plt.ylim(0,1400)
    plt.savefig('Graph2.png', bbox_inches ='tight',dpi =500)

    plt.show()