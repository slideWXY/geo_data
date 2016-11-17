#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:21:20 2016

@author: m_thelot
"""

# CREATE NEW FEATURES :
    

from geopy.geocoders import Nominatim
import pandas as pd
from geopy.distance import great_circle
    
def geo_feature(latitude, longitude):
    geolocator = Nominatim()
    coord = (str(latitude), str(longitude))
    if latitude + longitude == 0:
        return 'nan'
    else:
        location = geolocator.reverse(coord, language='en')
        return location.address

def df_geo_feature(df):
    """
    need a row latitude and longitude 
    """
    if 'latitude' not in df.columns:
        print "your df doesn't have a latitude columns !!!"
        return
        
    f = lambda x : geo_feature(x['latitude'],x['longitude'])    
    df['location'] = df.apply(f, axis=1)


def df_geo_create_features(df):
    # create news columns associate to the metrics list = [Town, Province, Country]
    df_geo_feature(df)

    # get the loc Country, Province and Town:
    df = pd.concat([df,df.location.apply(lambda x: pd.Series({'Town'      : 'nan' if x=='nan' else x.split(',')[-3],
                                            'Province'  : 'nan' if x=='nan' else x.split(',')[-2],
                                            'Country'   : 'nan' if x=='nan' else x.split(',')[-1]}))],
                                            axis=1, join_axes=[df.index], join='inner')
    return df    


def geo_distance(geo_1, geo_2):
    return great_circle(geo_1, geo_2).km

def event_id2latlong(df, event_id_i):
    # return a tuple (latitude,longitude) of the df[event_id]
    return tuple(df[df.event_id ==event_id_i][['latitude','longitude']].values[0])

def geo_maxdistance(df):
    # compute the max distance to know if the user is a globtrotter 
    event_id_lat_min = df[df.latitude != 0].min().event_id
    event_id_lat_max = df[df.latitude != 0].max().event_id
    event_id_long_min = df[df.longitude != 0].min().event_id
    event_id_long_max = df[df.longitude != 0].max().event_id
    
    event_id_to_choose = [event_id_lat_min,
                          event_id_lat_max,
                          event_id_long_min,
                          event_id_long_max]
                          
    dist_max = geo_distance( event_id2latlong(df, event_id_lat_min),
                             event_id2latlong(df, event_id_lat_max) )
    
    for i in range(1,4):
        #compute max dist with great_circle
        for j in range(0,i):
            dist_max_i = geo_distance( event_id2latlong(df, event_id_to_choose[i]),
                                       event_id2latlong(df, event_id_to_choose[j]))
            if dist_max<dist_max_i:
                dist_max = dist_max_i

    return dist_max
            
