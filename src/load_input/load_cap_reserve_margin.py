import pandas as pd
import os
import string

def count(columns):
    str1 = "CapRes"
    count = 0
    for i in  columns:
        i =str(i)
        if i.startswith(str1):
            count+=1
    return count
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
    index = 0
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







def load_cap_reserve_margin(setup:dict,path:str,inputs:dict):
    filename = "\Capacity_reserve_margin.csv"
    file_path = os.path.join(path,filename)

    df = pd.read_csv(file_path)
    columns = df.columns
    res = count(columns)
    name = "CapRes"
    first_col = findfirst(columns,name)
    last_col = findlast(columns,name)

    inputs["dfCapRes"] = float(df[:,first_col:last_col].values)
    inputs["NCapacityReserveMargin"] = res

    print(filename," Successfully Read!")

def load_cap_reserve_margin_trans(setup:dict,input:dict,network_var:pd.DataFrame):
    columns = network_var.columns
    name ="DerateCapRes"
    index_first = findfirst(columns,name)
    index_last = findlast(columns,name)
    dfDerateTransCapRes = network_var[:, index_first:index_last]
    input["dfDerateTransCapRes"] = float(dfDerateTransCapRes[dfDerateTransCapRes.isna])

    name = "CapRes_Excl"
    index_first  =findfirst(columns,name)
    index_last = findlast(columns, name)
    dfTransCapRes_excl = network_var[:,index_first:index_last]
    input["dfTransCapRes_excl"] = float(dfTransCapRes_excl[dfTransCapRes_excl.isna])









