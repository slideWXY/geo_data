#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:29:16 2016

@author: m_thelot
"""

# temporal analyse:
    
import pandas as pd
import numpy as np
import os


from data_loader import events

device_id = events.device_id.unique()

df_temp = pd.DataFrame({"device_id" : device_id} ).sample(n=8)

"""
# we create :
    nbr_differents_places : the number of differents places where the user uses an app
    
    gps_on_ratio : the ratio of activate GPS on all connections to app
    coord_gps : the gps coord
"""

#list_nbr_differents_places
list_gps_on_ratio = []

for index in df_temp.device_id:
    print index
    elements = events[events.device_id==index]
    nbr_differents_places = len(elements)
    
    elements = events[events.device_id==index]
    
    if elements.latitude.sum() == 0:
        gps_on_ratio = 0
    else:
        gps_on_ratio = elements['latitude'][elements.latitude != 0].count()*1. / nbr_differents_places

    list_gps_on_ratio.append(gps_on_ratio)

df_temp['ratio_gps_on'] = list_gps_on_ratio
    

