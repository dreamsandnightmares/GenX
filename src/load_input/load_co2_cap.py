import os
import pandas as pd

def findfirst(columns,str):
    str1= str
    index =0
    for i in columns:
        if i  ==str1:
            index =i
            break
        else:
            print('CapRes not in columns')
        return index


def findlast(columns,str):
    str1 = str
    i = 0
    flag  =-1
    while(i < len(columns)):
        if (str(i)==str1):
            flag = i
        i +=1
    if (flag ==-1):
        print('CapRes not in columns')
    else:
        return flag


def load_co2_cap(setup:dict,path:str,inputs:dict):
    filename = "\CO2_cap.csv"
    file_path = os.path.join(path,filename)

    inputs["dfCO2Cap"] = pd.read_csv(file_path)
    columns = inputs["dfCO2Cap"].columns
    name ="CO_2_Cap_Zone"
    index_first = findfirst(columns,name)
    index_last =findlast(columns,name)

    inputs["dfCO2CapZones"] = float(inputs["dfCO2Cap"][:,index_first:index_last])
    # inputs["NCO2Cap"] =



