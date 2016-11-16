#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:12:44 2016

@author: m_thelot
"""

import pandas as pd
import numpy as np
import os
from plot_and_viz import *


datafile = "/Users/m_thelot/notebooks/challenge/data/"

events = pd.read_csv(datafile + "events.csv", dtype={'device_id': np.str,
                                                     'event_id' : np.str})

gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id': np.str})


# show on a map
geo_plot(events, sample_size=100000)


def join_df(dict_df, key_column):
    result = pd.concat([df1, df4], axis=1)
    # return a dataframe when you select a column_name
    pass 
    
    
def traveling_distance():
    # compute a daily mean 
    pass

#gender_age_train.gender.value_counts().plot.pie(subplots=True, figsize=(8, 8))
#gender_age_train.group.value_counts().plot(kind='bar')




phone_brand_device_model.phone_brand.value_counts().plot(kind='bar')





