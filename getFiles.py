#!/usr/bin/env python3
import csv
import numpy as np
import sys
import re
from flask import jsonify
import pprint
import json
import time
pp = pprint.PrettyPrinter()




def birthRateAdjust(popFile, moralityFile):
    pattern = '(\S+)\s+(\S+)'
    #moralityFile = './data_files/Mortality_Rate_US.csv'
    #popFile = './data_files/totalPop.txt'
    pattern_date = '%m/%d/%Y'
    rateArray = []
    dataArray = []
    dateArray = []
    deathsPerYear = []
    for i, line in enumerate(open(moralityFile)):
        for match in re.finditer(pattern, line):
            date = match.group(1)
            rate = match.group(2)
            # CSV files have a BOM at the begining of the file 
            date = date.encode('utf-8').decode('utf-8-sig')
            epoch = int(time.mktime(time.strptime(date,pattern_date)))
            epoch = epoch * 1000
            dateArray.append(epoch)
            rateArray.append(float(rate.replace(",",'')))
    pp.pprint(rateArray)
    pp.pprint(dateArray)
    for ii, line in enumerate(open(popFile)):
        for match in re.finditer(pattern, line):
            currentPop = match.group(2)
            currentPop = float(currentPop)
            deathsPerYear.append((rateArray[ii] * currentPop)/10000)
            dataArray = [[dateArray[ii], deathsPerYear[ii]]] + dataArray
    pp.pprint(dataArray)
    json_dataArray = json.dumps(dataArray)
    return dataArray, json_dataArray






def get_US2000(filename, pattern, padFlag):
    diclist = []
    data_array = []
    pattern_date = '%m/%d/%Y'
    print('filename = ', filename)
    print('pattern = ', pattern)
    for i, line in enumerate(open(filename)):
        print('LINE = ', line)
        for match in re.finditer(pattern, line):
            day = match.group(1)
            month = match.group(2)
            year = match.group(3)
            data = match.group(4)
            data = data.replace(",",'')
            data = float(data)
            date_time = day+'/'+month+'/'+year
            #print(date_time)
            #print(year)
            epoch = int(time.mktime(time.strptime(date_time,pattern_date)))
            epoch = epoch * 1000
            current_data = [epoch,data]
            data_array = [current_data] + data_array
            dic = {
                "date": date_time,
                "data": data,
                }
            diclist.append(dic)
    N = 115;
    if( len(data_array) < N and padFlag == 1):
        zeros_needed = N - len(data_array)
        z = [0.0,0.0]
        for i in range(0, zeros_needed):
            data_array = data_array + [z]

    json_dic = json.dumps(diclist)
    json_array = json.dumps(data_array)
    return diclist, json_dic, data_array, json_array

def getDebtPerPerson(popArray, debtArray):
    debtPerPersonArray = [];
    for i in range(len(debtArray)):
        print("i = " ,i)
        debtPerPerson = debtArray[i][1]/popArray[i][1]
        print("debt per person = " , debtPerPerson)
        print( "debt date = ", debtArray[i][0])
        epochDebt = debtArray[i][0]
        data_arr = [epochDebt,debtPerPerson]
        debtPerPersonArray = [data_arr] + debtPerPersonArray

    pp.pprint(debtPerPersonArray)
    return json.dumps(debtPerPersonArray)


"""
pattern_regrex = ('(?i)(\S+\s\S+\s\S+)\W+(\S+)\W+(\S+)\W+(\S+)')
diclist = get_CSV("'./data_files/US_population.txt', pattern_regrex)
pp.pprint(diclist)

pattern_2000 = ('(?i)(\S+)\s+(\S+)')
diclist2000 = get_US2000('./data_files/US_population_2000-Current.txt', pattern_2000)
pp.pprint(diclist2000)
"""
deathPerYear = birthRateAdjust('./data_files/totalPop.txt','./data_files/Mortality_Rate_US.csv')

