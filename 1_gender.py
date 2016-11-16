#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:39:21 2016

@author: m_thelot
"""
import pandas as pd
import numpy as np


datafile = "/Users/m_thelot/notebooks/challenge/data/"
gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id': np.str})
events = pd.read_csv(datafile + "events.csv", dtype={'device_id': np.str, 'event_id' : np.str})


M22 = gender_age_train[gender_age_train['group']=='M22-']


# device_id
M22_events = events[events['device_id'] == list(M22['device_id'])]

def remove_in_list(list_, lists_el2remove):
    for i in lists_el2remove:
        list_.remove(i)
    return
    
def list_union(df1,df2, column_name):
    "return union of 2 lists of the column_name"
    list1 = list(df1[column_name])
    list2 = list(df2[column_name])

    return list(set().union(list1,list2))

def dfselector(df_events, column_key, elements):
    "return a df like : df_out = df_events[df_events[column_key] == elements ]"
    "Be sure that elements exist in the df_events ==> cf select_events function"
    df_use = df_events.copy()
    df_use.index = df_use[column_key]
    df = df_events[df_events[column_key] == elements[0] ]
    df_use.drop([elements[0]], inplace=True)
    for element in elements[1:]:
        df1 = df_use[df_use[column_key] == element ]
        df = pd.concat([df,df1])
        df_use.drop([elements[0]], inplace=True)
    return df

        
def select_events( df, df_events, column_key):
    elements = list_union(df,df_events, column_name=column_key)
    return  dfselector(df_events, column_key, elements)

df1 = M22.copy()
M22_events = select_events( df1, events, column_key='device_id')
    
M22_events = select_events(M22,events,column_key='device_id')