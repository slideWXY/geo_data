#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:09:37 2016

@author: m_thelot
"""

import os 
import pandas as pd
import numpy as np
import re
from data_categories import *


datafile = "/Users/m_thelot/notebooks/challenge/data/"

events = pd.read_csv(datafile + "events.csv", dtype={'device_id': np.str, 'event_id' : np.str})
gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id' : np.str})
app_events = pd.read_csv(datafile + "app_events.csv", dtype={'event_id' : np.str, 'app_id' : np.str})
app_labels = pd.read_csv(datafile + "app_labels.csv", dtype={'app_id' : np.str,'label_id' : np.str})

# gender_age_test = pd.read_csv(datafile + "gender_age_test.csv", dtype={'device_id': np.str})
# gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id': np.str})

label_categories = pd.read_csv(datafile + "label_categories.csv", dtype={'label_id' : np.str})

label_sample = label_categories.sample(n =100)
app_label_sample = app_labels.sample(n =100)

def df_joinner(df1,df2, join_axes, del_col=""):
    df1.index = df1[join_axes]
    df2. index = df2[join_axes]
    df = pd.concat([df1,df2],axis=1, join_axes=[df1.index], join='inner')
    if del_col:
        df = df.drop(del_col, 1)
    return df
df_ = df_joinner(app_labels,label_categories, join_axes= 'label_id', del_col='label_id')
#df_ = df_joinner(df_, app_events, join_axes= 'app_id', del_col = 'app_id')
df_.to_csv(path_or_buf=datafile+'app_join.csv')

# create a file of 2.5 Go
#df_1 = df_joinner(app_events,events, join_axes= 'event_id', del_col='event_id')
#df_1.to_csv(path_or_buf=datafile+'events_join.csv')

