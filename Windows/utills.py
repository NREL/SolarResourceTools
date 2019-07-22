#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:51:52 2019

@author: rgupta2
"""
import os
import pandas as pd

def readList(name): # pass the *.txt file name
    f=(open(name, 'r'))
    val=(f.read()).split()
    #os.remove(name)

    return val
'''
def writeExcel(df1, df2, df3, df4, name1, name2, name3, name4):
    writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

    df1.to_excel(writer, sheet_name= name1)
    df2.to_excel(writer, sheet_name= name2, startrow=16)
    df3.to_excel(writer, sheet_name= name3)
    df3.to_excel(writer, sheet_name= name4)

    writer.save()'''