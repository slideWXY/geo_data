#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:14:43 2016

@author: m_thelot
"""
import os 
import pandas as pd
import numpy as np
from itertools import compress
from data_categories import *
from plot_and_viz import plot_corr


datafile = "/Users/m_thelot/notebooks/challenge/data/"

events = pd.read_csv(datafile + "events.csv", dtype={'device_id': np.str, 'event_id' : np.str})
gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id' : np.str})
app_events = pd.read_csv(datafile + "app_events.csv", dtype={'event_id' : np.str, 'app_id' : np.str})
app_labels = pd.read_csv(datafile + "app_labels.csv", dtype={'app_id' : np.str,'label_id' : np.str})

# gender_age_test = pd.read_csv(datafile + "gender_age_test.csv", dtype={'device_id': np.str})
# gender_age_train = pd.read_csv(datafile + "gender_age_train.csv", dtype={'device_id': np.str})

label_categories = pd.read_csv(datafile + "label_categories.csv", dtype={'label_id' : np.str})

label_sample = label_categories.head(100)
#app_label_sample = app_labels.head(100)
#app_event_sample = app_events.head(100)



# create a ywords with all words of list_sample:
list_sample = list(label_sample.category.replace(np.nan, 'nan', regex=True))
 
# LABELS CATEGORIES TO CATEGORIES 
y_words = create_ywords(list_sample,3)
y_labels = label_matrix(list_sample, y_words)
df_score = pd.DataFrame(data=y_labels, columns=y_words, index= list_sample)

groups = {}
for col in df_score.columns:
    group = list(df_score[df_score[col]==1].index)
    if len(group)>1:
        groups[col] = group

# Search a proximity between groups:

# first create a matrix of zeros to have a good representation of proximity
N = len(y_words)
groups_matrix = create_matrix(N, N)
df_groups = pd.DataFrame(data=groups_matrix, columns=y_words ,index=y_words )

def selecting_in_list(list_, selector):
    "selector is a list of Bool and select specific elements in list_"
    return list(compress( list_, selector))

def group_score(df_groups, list_):
    for i in list_:
        for j in list_:
            df_groups.loc[i][j]+=1
    return


lines = map(list, df_score.values)
columns = list(df_score.columns)
for line in lines:
    if sum(line)>1:
        names_groups = selecting_in_list(columns, line)
        group_score(df_groups, names_groups)
        

df_corr = df_groups.corr(method='pearson', min_periods=1)

# plot_corr(df_corr)

# Make a Hierarchic cluster :



# Create test_measures to compute scor elements
def scoring(letter1,letter2):
    if letter1 == letter2:
        return 5
    else:
        return -2

def score_root_words(element, word_label):
    " return a score of similarity/root between element and word_label"
    " for a same letter the score win 3. If the letter doesn't match the score lose 1"
    " if element have the exact word_label the score is equal to 3*(len of word_label ) + 20"

    len_word = len(element)
    len_label = len(word_label)
    
    if element == word_label:
        score = 100
    elif len_word>len_label:
        word_label += " "*(len_word - len_label)
        score = sum(map(scoring, element, word_label))
    else:
        element += " "*(len_label - len_word)
        score = sum(map(scoring, element, word_label))

    return score

def df_2_score(df_):
    
    for col in df_.columns:
        values= []
        for element in df_.index:
            values.append( score_root_words( regex_lower(element), col) )
        df_[col] = values
    return

    
def create_df(matrix, index, col):
    if matrix==0:
        N = len(index)
        M = len(col)
        matrix = create_matrix(N, M)
    return pd.DataFrame(data = matrix, index=index, columns=col)


df_similarity = create_df(matrix=0, index=df_groups.columns, col=df_groups.columns)
df_2_score(df_similarity)



def labelize_with_list(list_elements):
    " return a str of all words in list_element join by '-' "
    return "-".join(list_elements)
    
def unique_in_list(list_):
    return list(set(list_))
    
def join_groups(dict_, keys):
    keys = unique_in_list(keys)
    new_keys = labelize_with_list(keys )
    list_values = []
    for key in keys:
        list_values.append(dict_[key])
        
    list_values = flat_list(list_values)
    list_values = unique_in_list(list_values)
    
    return new_keys, list_values
    


