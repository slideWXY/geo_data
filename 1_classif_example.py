#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 08:07:15 2016

@author: m_thelot
"""

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

X_train = np.array(["new york is a hell of a town",
                    "new york was originally dutch",
                    "the big apple is great",
                    "new york is also called the big apple",
                    "nyc is nice",
                    "people abbreviate new york city as nyc",
                    "the capital of great britain is london",
                    "london is in the uk",
                    "london is in england",
                    "london is in great britain",
                    "it rains a lot in london",
                    "london hosts the british museum",
                    "new york is great and so is london",
                    "i like london better than new york"])
y_train = [[0],[0],[0],[0],[0],[0],[1],[1],[1],[1],[1],[1],[0,1],[0,1]]
y_trainn = MultiLabelBinarizer().fit_transform(y_train)
X_test = np.array(['nice day in nyc',
                   'welcome to london',
                   'hello welcome to new york. enjoy it here and london too'])   
target_names = ['New York', 'London']

classifier = Pipeline([
    ('vectorizer', CountVectorizer(ngram_range=(1,2))),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(LinearSVC()))])
classifier.fit(X_train, y_trainn)
predicted = classifier.predict(X_test)

def labelz(list_):
    return np.where(list_==1)[0]

for item, labels in zip(X_test, predicted):
    print '%s => %s' % (item, ', '.join(target_names[x] for x in labelz(labels)))

def line_response():
    return
    
def create_ypred():
    "create a matrix of predictive