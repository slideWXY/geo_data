#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:23:42 2016

@author: m_thelot
"""

import pandas as pd
import numpy as np
from itertools import compress
import re

# Labels to categories functions:

def regex_lower(word_expression):
    "transform a word_expression to lower"
    return str(word_expression).lower()
    
def list2lower(list_):
    #transfom a list_sample to a very big list of unqiue words
    return map(regex_lower, list_)    

def split_str(str_expression, str_to_split):
    "split a str txt with the str_to_split method"
    return str_expression.split(str_to_split)
def flat_list(list_of_list):
    "transform a list of lists in a big list"
    return [item for sublist in list_of_list for item in sublist]

def list2split(list_, list_str_to_split):
    "return unique words of list_ after appling the list_str_to_split transformations"
    for str_to_split in list_str_to_split:
        if str_to_split == '-':
            list_ = map(lambda x: x.replace('-',' '), list_)
        else:
            list_ = map(split_str, list_, str_to_split)
            list_ = flat_list(list_)
    return list(set(list_))    
    
def create_ywords(list_sample,size_min_word):
    list_sample = list2lower(list_sample)
    list_sample = list2split(list_sample, ['-',' '])
    
    return filter(lambda x: len(x)>=size_min_word, list_sample)

def matching(expr, word_2_match):
    " return True if word_2_match matchs with expr else return False "
    "Becarful !! if the word_2_match is a letter this funtion will match all expressions with the letter"
    if word_2_match in expr:
        return 1
    else:
        return 0
    
def list_matching(list_expr, word_2_match):
    list_ = []
    for i in list_expr:
        list_.append( matching(regex_lower(i), word_2_match))
    return list_

def create_matrix(nbr_lines, nbr_columns):
    " create a zeros_matrix with nbr_lins * nbr_columns"
    return np.zeros((nbr_lines, nbr_columns))
    
def label_matrix(list_df_column, y_words):
    label_mat = create_matrix( nbr_lines=len(list_df_column), nbr_columns=len(y_words))
    for i, word in enumerate(y_words):
        label_mat[:,i] = list_matching(list_df_column, word)
    return label_mat

    
def selecting_in_list(list_, selector):
    "selector is a list of Bool and select specific elements in list_"
    return list(compress( list_, selector))

def group_score(df_groups, list_):
    for i in list_:
        for j in list_:
            df_groups.loc[i][j]+=1
    return

# Create test_measures to compute scor elements
def scoring(letter1,letter2):
    if letter1 == letter2:
        return 5
    else:
        return -2

def score_root_words(element, word_label):
    " return a score of similarity/grammar_root between element and word_label"
    " for a letter at the same position the score earns 5. If the letter doesn't match the score loses 2"
    " if element have the exact word_label the score is equal to 100"

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