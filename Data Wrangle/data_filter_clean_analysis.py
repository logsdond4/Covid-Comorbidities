# -*- coding: utf-8 -*-
"""
Author: Dan Logsdon
Date: 10/11/2020

Description: This code analyzes the CDC's data related to Covid deaths and 
comorbidities.

Limitations: The CDC did not provide record level data, which means that it is
impossible to do analysis by individual ICD10 code. 

"""

#Package Imports
import pandas as pd
import os

#%% File Import
root = os.path.dirname(os.path.dirname(__file__)) #root folder
src = root + '\\src' #source folder
file = src + '\\Covid-19_comorbidities.csv' #input file
df=pd.read_csv(file)



#%% Functions
def df_filter(df):
    df=df[df.State=='US'] #removed state data
    df=df[df['Age Group']== 'All Ages'] #remove ages
    return df

def df_calc(df):
    #new row for COVID-19 deaths with no comorbidities, CDC specified this was 6% of total
    new_row = {'Condition Group':'Covid-19 Only', 'ICD10_codes':'U071', 'Number of COVID-19 Deaths':int(total_deaths*0.06)}
    df = df.append(new_row, ignore_index=True)
    df['percent_deaths']=df['Number of COVID-19 Deaths']/total_deaths*100
    return df

#%% Filter
df=df_filter(df)

#%% Globals    
total_deaths=int(df[df['Condition Group']=='COVID-19']['Number of COVID-19 Deaths'])

#%% Analysis
df=df_calc(df)

