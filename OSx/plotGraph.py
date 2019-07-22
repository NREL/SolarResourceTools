#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:04:51 2019

@author: rgupta2
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot(report, componentList, InstrumentName):
    startPoint = (report.shape[1]-1)-len(componentList)
    stopPoint = startPoint + len(componentList)
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
    plt.grid(True)
    plt.savefig('Graph.png', bbox_inches ='tight', dpi=1000)
    plt.show()
   
#plot(report, componentList, InstrumentName)


def plotUncertainty(report, InstrumentName):
    firstDate = report[0:1]['DATE'][0]
    temp = report[report['DATE']==firstDate]
    x = (temp['Unnamed: 1'].map(str))
    y=temp[InstrumentName][:12]
    yerr = temp['ExpUncert Wm^-2'][:12]
    plt.errorbar(x.values,y, yerr, errorevery=1, ecolor ='red',color='green')
    plt.tick_params(axis='x', labelrotation=90)
    plt.xlabel('Time')
    plt.ylabel('Irradiance W/m^2')
    green_patch = mpatches.Patch(color='green', label='Irradiance in W/m^2')
    red_patch = mpatches.Patch(color='red', label='Expanded uncertainty values at 95% conf. level')

    plt.legend(loc = 2,handles=[green_patch,red_patch],bbox_to_anchor=(0,1))
    plt.grid(True)
    plt.ylim(0,1400)
    plt.savefig('Graph2.png', bbox_inches ='tight', dpi=1000)
    plt.show()
