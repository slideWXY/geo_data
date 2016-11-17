#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 14:31:09 2016

@author: m_thelot
"""
import os 
import pandas as pd
import numpy as np


datafile = "/Users/m_thelot/notebooks/challenge/data/"

events = pd.read_csv(datafile + "events.csv", dtype={'device_id': np.str,
                                                     'event_id' : np.str})
gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id': np.str})

app_events = pd.read_csv(datafile + "app_events.csv", dtype={'event_id' : np.str,
                                                             'app_id'   : np.str})

app_labels = pd.read_csv(datafile + "app_labels.csv", dtype={'app_id': np.str,
                                                              'label_id' : np.str})

gender_age_test = pd.read_csv(datafile + "gender_age_test.csv", dtype={'device_id': np.str})
gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id': np.str})

label_categories = pd.read_csv(datafile + "label_categories.csv", dtype={'label_id' : np.str})

phone_brand_device_model = pd.read_csv(datafile + "phone_brand_device_model.csv", dtype={'device_id': np.str})

sample_submission = pd.read_csv(datafile + "sample_submission.csv")