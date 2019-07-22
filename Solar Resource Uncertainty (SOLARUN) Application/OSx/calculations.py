#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:36:02 2019

@author: rgupta2
"""

import math
import pandas as pd
import formUI
import utills
#from scipy.stats import norm

def gatherFormData(columnlist):
    formData=pd.DataFrame()
    for i in columnlist:
        formUI.takeParams(i)
        newVar = utills.readList('temp')
        formData[i] = newVar
    formData = formData.transpose()
    formData = formData.reset_index(level=0)
    formData = formData.rename(index=str, columns={'index':'Component',0:'variable', 1:'uncertaintyType',2:'distribution',3:'symmetry',4:'incAnalysis'})
    return formData

def calExpandeduncertainty(ComponentList, InstrumentList, InstrumentName):
    uncertainty = pd.DataFrame({'Component':ComponentList},columns= ['Component'])
    expUncert=[]
    for i in ComponentList:
        expUncert.append(list(InstrumentList[InstrumentList['Instrument']== InstrumentName][i])[0])
    for i in range(len(expUncert)):
        if (type(expUncert[i])==str):
            expUncert[i]=0
    
    uncertainty['Expanded uncertainty'] = expUncert
    
    return uncertainty

def calStandardUncert(formData, uncertainty):
    stanUncert =[]
    for i in (uncertainty['Component']):
        current = formData[formData['Component']==i]
        expnadedUncert = float(uncertainty[uncertainty['Component']==i]['Expanded uncertainty'])
        if (current['symmetry'][0] =='Symmetric'):
            if (current['incAnalysis'][0]=='Yes'):
                if (current['distribution'][0]== 'Normal'):
                     stanUncert.append(expnadedUncert/1.96)
                else:
                    if (current['distribution'][0]== 'Rectangular'):
                         stanUncert.append(expnadedUncert/math.sqrt(3))
                    else:
                        if (current['distribution'][0]== 'Triangular'):
                             stanUncert.append(expnadedUncert/math.sqrt(6))
                        else:
                            if (current['distribution'][0]== 'U-shaped'):
                                 stanUncert.append(expnadedUncert/math.sqrt(2))
            else:
                stanUncert.append(0)
        else:
            if (current['incAnalysis'][0]=='Yes'):
                if (current['distribution'][0]== 'Normal'):
                     stanUncert.append(0.5 * expnadedUncert/1.64)
                else:
                    if (current['distribution'][0]== 'Rectangular'):
                         stanUncert.append(0.5 * expnadedUncert/math.sqrt(3))
                    else:
                        if (current['distribution'][0]== 'Triangular'):
                             stanUncert.append(0.5 * expnadedUncert/math.sqrt(6))
                        else:
                            if (current['distribution'][0]== 'U-shaped'):
                                 stanUncert.append(0.5 * expnadedUncert/math.sqrt(2))
            else:
                stanUncert.append(0)
    uncertainty['Standard uncertainty'] = stanUncert
    return uncertainty


def createColWithSelection(formData):
    #formData['newName'] = 'SUS_'+formData['Component']+'_'+formData['variable']+'_'+'[W/m²]'
    tempList =[]
    for i in formData['Component']:
        current = formData[formData['Component']==i]
        if (current['variable'][0]=='E'):
            tempList.append('SUS_'+current['Component'][0]+'_'+current['variable'][0]+'_[W/m²]'[0])
            #formData[formData['Component']==i]['newName']='SUS_'+formData['Component']+'_'+formData['variable']+'_[W/m²]'
            #formData['newName'] = 'SUS_'+formData['Component']+'_'+formData['variable']+'_[W/m²]'
        else:
            if (current['variable'][0]=='V'):
                tempList.append('SUS_'+current['Component'][0]+'_'+current['variable'][0]+'_[µV]'[0])
                #formData[formData['Component']==i]['newName'] = 'SUS_'+formData['Component']+'_'+formData['variable']+'_[µV]'
            else:
                if (current['variable'][0]=='S'):
                    tempList.append('SUS_'+current['Component'][0]+'_'+current['variable'][0]+'_[µV/(W/m²)]'[0])
                    #formData[formData['Component']==i]['newName'] = 'SUS_'+formData['Component']+'_'+formData['variable']+'_[µV/(W/m²)]'
    formData['newName'] = tempList
    return formData

def calculateuncertainty(InstrumentName, data, InstrumentList, formData, uncertainty):
    responsivity = float(InstrumentList[InstrumentList['Instrument']==InstrumentName]['Responsivity (uv/W/m^2)'])
    dataLoggerAccuSetup = float(InstrumentList[InstrumentList['Instrument']==InstrumentName]['Data Logger Accuracy and Setup (CR3000)'])

    #InstrumentList = InstrumentList['Instrument'].tolist()
    calFinal= pd.DataFrame(data.iloc[:,0:3])
    calFinal[InstrumentName]=data[InstrumentName]
    calFinal['Voltage [uv]'] = calFinal[InstrumentName]*responsivity
    calFinal['Uv [uV]'] = (0.0004*calFinal['Voltage [uv]']+dataLoggerAccuSetup)/math.sqrt(3)
    calFinal['Senitivity Coefficient Cv [1/uv/w/m^2]'] = 1/responsivity
    calFinal['Senitivity Coefficient Cs [(Wm^-2)^2 uV^-1]'] = abs(-(calFinal['Voltage [uv]'])/(responsivity**2))
    
    #number of columns till now
    cNum = len(calFinal.columns)
    
    # SUS for Standard uncertainty and squares
    formData = createColWithSelection(formData)
    
    for i in formData['newName']:
        current = formData[formData['newName']==i]
        StanUncert = float(uncertainty[uncertainty['Component']==current['Component'][0]]['Standard uncertainty'])

        if (current['uncertaintyType'][0] =='Absolute'):
            calFinal[i] = (StanUncert)**2#list(uncertainty[uncertainty['Component']==i]['Standard uncertainty'])[0]
        else:
            if (current['variable'][0]== 'S'):
                calFinal[i] =((StanUncert/100)*responsivity)**2#list(uncertainty[uncertainty['Component']==i]['Standard uncertainty'])[0]
            else:
                if(current['variable'][0]== 'E'):
                    calFinal[i] = ((StanUncert/100)*calFinal[InstrumentName])**2
                else:
                    if(current['variable'][0]== 'V'):
                        calFinal[i] = 0
                        
    #collecting colnames for further calculations
    tempCol= calFinal.columns[cNum:]
    
    calFinal['SUS_relative_V'] = calFinal['Uv [uV]']
    calFinal['SUS_relative_S'] = 0
    for i in (formData['newName']):
        current = formData[formData['newName']==i]
        if (current['variable'][0]== 'S'):
            calFinal['SUS_relative_S'] = calFinal['SUS_relative_S']+calFinal[i]
    calFinal['SUS_relative_S']=(calFinal['SUS_relative_S'])**0.5
    
    calFinal['SUS_relative_E'] = 0
    for i in (formData['newName']):
        current = formData[formData['newName']==i]
        if (current['variable'][0]== 'E'): calFinal['SUS_relative_E'] = calFinal['SUS_relative_E']+calFinal[i]
    calFinal['SUS_relative_E']=(calFinal['SUS_relative_E'])**0.5
    
    # Combined uncertainty 
    calFinal['Combined Uncertainty Wm^-2'] = ((calFinal['SUS_relative_V']*calFinal['Senitivity Coefficient Cv [1/uv/w/m^2]'])**2+(calFinal['SUS_relative_S']*calFinal['Senitivity Coefficient Cs [(Wm^-2)^2 uV^-1]'])**2 + (calFinal['SUS_relative_E']*1)**2)**0.5
    calFinal['Combined Uncertainty %'] = (calFinal['Combined Uncertainty Wm^-2']/calFinal[InstrumentName])*100
    
    # Expanded uncertainty
    
    normalKfactor = 1.96
    #coverage = (1-(2*norm.cdf(-normalKfactor)))*100
    calFinal['ExpUncert Wm^-2'] = normalKfactor * calFinal['Combined Uncertainty Wm^-2']
    calFinal['ExpUncert % of Reading'] = (calFinal['ExpUncert Wm^-2']/calFinal[InstrumentName])*100
    
    cNum = len(calFinal.columns)

    # Used only for percent contribution calculation - UPCAL
    for i in tempCol:
        current = formData[formData['newName']==i]
        nColName =i.replace('SUS_', 'UPCAL_')
        if (current['variable'][0]== 'V'):
            if ('Data Logger' in i):
                calFinal[nColName] = calFinal['Uv [uV]'] * calFinal['Senitivity Coefficient Cv [1/uv/w/m^2]']
            else:
                calFinal[nColName] =  calFinal[i] * calFinal['Senitivity Coefficient Cv [1/uv/w/m^2]']
        else:
            if (current['variable'][0]== 'S'):
                if ('Data Logger' in i):
                    pass
                else:
                        calFinal[nColName] =  ((calFinal[i])**0.5) * calFinal['Senitivity Coefficient Cs [(Wm^-2)^2 uV^-1]']
            else:
                if (current['variable'][0]== 'E'):
                    if ('Data Logger' in i):
                        pass
                    else:
                        calFinal[nColName] =  ((calFinal[i])**0.5) * 1
    tempCol= calFinal.columns[cNum:]

    calFinal['Sum of Stand Uncert * Data Logger'] = calFinal.values[:,cNum:].sum(axis=1)
    
    # Contribution % - Cont %
    cNum = len(calFinal.columns)
    for i in tempCol:
        current = formData[formData['newName']==i]
        nColName = i.replace('UPCAL_','Cont %_')
        calFinal[nColName] = (calFinal[i]/calFinal['Sum of Stand Uncert * Data Logger'])*100
    calFinal['Total %'] = calFinal.values[:,cNum:].sum(axis=1)
    
    
    return calFinal

def finalUncertPercentage(calFinal,InstrumentName):
    maxIrradiance = max(calFinal[InstrumentName])
    indexMaxIrr = list(calFinal[InstrumentName]).index(maxIrradiance)
    maxExpUncert= calFinal['ExpUncert Wm^-2'][indexMaxIrr]
    finaluncertainty = (maxExpUncert/maxIrradiance)*100
    data = pd.DataFrame({'Selected Option': [InstrumentName],'Max Irradiance':[str( maxIrradiance) + ' W/m^2'], 'Expanded uncertainty': [maxExpUncert] ,'uncertainty %' : [finaluncertainty] })
    return data
