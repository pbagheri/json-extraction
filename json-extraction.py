# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:10:56 2019

@author: payam.bagheri
"""

import pandas as pd
from os import path
import ast

dir_path = path.dirname(path.dirname(path.abspath(__file__)))
data = pd.read_csv(dir_path + '/0_input_data/2057-json-data.csv')

data.columns

def dicter(anonstring):
        try:
            ev = ast.literal_eval(anonstring)
            return ev
        except ValueError:
            corrected = "\'" + anonstring + "\'"
            ev = ast.literal_eval(corrected)
            return ev

dicter(data.full_exercise.iloc[0])

datakeys = pd.DataFrame(columns= ['respid','first', 'categoryID11',  'productListing11', 'productID11', 'categoryID12',  'productListing12', 'productID12', 'categoryID13',  'productListing13', 'productID13', 'second','categoryID21',  'productListing21', 'productID21', 'categoryID22',  'productListing22', 'productID22', 'categoryID23',  'productListing23', 'productID23', 'third','categoryID31',  'productListing31', 'productID31', 'categoryID32',  'productListing32', 'productID32', 'categoryID33',  'productListing33', 'productID33', 'recommendationsToShow1', 'recommendationsShown1', 'cartpid1', 'cartquant1', 'recommendationsToShow2', 'recommendationsShown2', 'cartpid2', 'cartquant2', 'recommendationsToShow3', 'recommendationsShown3', 'cartpid3', 'cartquant3'], index = data.index)
datakeys.respid = data.respid

#first.apply(lambda x: dicter(x))
for i in data.index:    
    if len(data.full_exercise.iloc[i]) != 0:
        #print(i)
        datakeys['first'][i] = dicter(data.full_exercise.iloc[i])
        if str(datakeys['first'].iloc[i]["addToCartModal"]) != 'nan':
            k = 1
            l = 1
            for j in range(len(datakeys['first'].iloc[i]["addToCartModal"])):
                if (datakeys['first'].iloc[i]["addToCartModal"][j]['event'] == 'Show') and ('categoryID' in list(datakeys['first'].iloc[i]["addToCartModal"][j].keys())):
                    nam1 = 'categoryID1' + str(k)
                    nam2 = 'productListing1' + str(k)
                    k += 1
                    datakeys[nam1][i] = datakeys['first'].iloc[i]["addToCartModal"][j]['categoryID']
                    datakeys[nam2][i] = datakeys['first'].iloc[i]["addToCartModal"][j]['productListing']
                if (datakeys['first'].iloc[i]["addToCartModal"][j]['event'] == 'Click')  and ('productID' in list(datakeys['first'].iloc[i]["addToCartModal"][j].keys())):
                    nam1 = 'productID1' + str(l)
                    l += 1
                    datakeys[nam1][i] = datakeys['first'].iloc[i]["addToCartModal"][j]['productID']
    datakeys['recommendationsToShow1'][i] = datakeys['first'].iloc[i]['recommendationsToShow']
    datakeys['recommendationsShown1'][i] = datakeys['first'].iloc[i]['recommendationsShown']
    if len(datakeys['first'].iloc[i]['cart']) != 0:
        cartids = []
        cartquants = []
        for m in range(len(datakeys['first'].iloc[i]['cart'])):
            cartids.append(datakeys['first'].iloc[i]['cart'][m]['productID'])
            cartquants.append(datakeys['first'].iloc[i]['cart'][m]['quantity'])
        datakeys['cartpid1'][i] = cartids
        datakeys['cartquant1'][i] = cartquants

        
for i in data.index:    
    if  str(data.second_showing.iloc[i]) != 'nan':
        #print(i)
        datakeys['second'][i] = dicter(data.second_showing.iloc[i])
        if str(datakeys['second'].iloc[i]["addToCartModal"]) != 'nan':
            k = 1
            l = 1
            for j in range(len(datakeys['second'].iloc[i]["addToCartModal"])):
                if (datakeys['second'].iloc[i]["addToCartModal"][j]['event'] == 'Show') and ('categoryID' in list(datakeys['second'].iloc[i]["addToCartModal"][j].keys())):
                    nam1 = 'categoryID2' + str(k)
                    nam2 = 'productListing2' + str(k)
                    k += 1
                    datakeys[nam1][i] = datakeys['second'].iloc[i]["addToCartModal"][j]['categoryID']
                    datakeys[nam2][i] = datakeys['second'].iloc[i]["addToCartModal"][j]['productListing']
                if (datakeys['second'].iloc[i]["addToCartModal"][j]['event'] == 'Click')  and ('productID' in list(datakeys['second'].iloc[i]["addToCartModal"][j].keys())):
                    nam1 = 'productID2' + str(l)
                    l += 1
                    datakeys[nam1][i] = datakeys['second'].iloc[i]["addToCartModal"][j]['productID']
    if str(datakeys['second'].iloc[i]) != 'nan':
        datakeys['recommendationsToShow2'][i] = datakeys['second'].iloc[i]['recommendationsToShow']
        datakeys['recommendationsShown2'][i] = datakeys['second'].iloc[i]['recommendationsShown']
        if len(datakeys['second'].iloc[i]['cart']) != 0:
            cartids = []
            cartquants = []
            for m in range(len(datakeys['second'].iloc[i]['cart'])):
                cartids.append(datakeys['second'].iloc[i]['cart'][m]['productID'])
                cartquants.append(datakeys['second'].iloc[i]['cart'][m]['quantity'])
            datakeys['cartpid2'][i] = cartids
            datakeys['cartquant2'][i] = cartquants

for i in data.index:    
    if  str(data.last_showing.iloc[i]) != 'nan':
        #print(i)
        datakeys['third'][i] = dicter(data.last_showing.iloc[i])
        if str(datakeys['third'].iloc[i]["addToCartModal"]) != 'nan':
            k = 1
            l = 1
            for j in range(len(datakeys['third'].iloc[i]["addToCartModal"])):
                if (datakeys['third'].iloc[i]["addToCartModal"][j]['event'] == 'Show') and ('categoryID' in list(datakeys['third'].iloc[i]["addToCartModal"][j].keys())):
                    nam1 = 'categoryID3' + str(k)
                    nam2 = 'productListing3' + str(k)
                    k += 1
                    datakeys[nam1][i] = datakeys['third'].iloc[i]["addToCartModal"][j]['categoryID']
                    datakeys[nam2][i] = datakeys['third'].iloc[i]["addToCartModal"][j]['productListing']
                if (datakeys['third'].iloc[i]["addToCartModal"][j]['event'] == 'Click')  and ('productID' in list(datakeys['third'].iloc[i]["addToCartModal"][j].keys())):
                    nam1 = 'productID3' + str(l)
                    l += 1
                    datakeys[nam1][i] = datakeys['third'].iloc[i]["addToCartModal"][j]['productID']
    if str(datakeys['third'].iloc[i]) != 'nan':
        datakeys['recommendationsToShow3'][i] = datakeys['third'].iloc[i]['recommendationsToShow']
        datakeys['recommendationsShown3'][i] = datakeys['third'].iloc[i]['recommendationsShown']
        if len(datakeys['third'].iloc[i]['cart']) != 0:
            cartids = []
            cartquants = []
            for m in range(len(datakeys['third'].iloc[i]['cart'])):
                cartids.append(datakeys['third'].iloc[i]['cart'][m]['productID'])
                cartquants.append(datakeys['third'].iloc[i]['cart'][m]['quantity'])
            datakeys['cartpid3'][i] = cartids
            datakeys['cartquant3'][i] = cartquants
        

datakeys.to_csv(dir_path + '/0_output/datakeys.csv')
