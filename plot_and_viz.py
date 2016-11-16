#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:35:57 2016

@author: m_thelot
"""

import matplotlib.pyplot as plt
import seaborn as sns 
from mpl_toolkits.basemap import Basemap
import numpy as np

def geo_plot(df_with_loc, sample_size=100000):
    # data need to have longitude and latitude columns. You could select a sample_size
    if sample_size:
        df_events_sample = df_with_loc.sample(n=sample_size)
    else: 
        df_events_sample = df_with_loc
    
    plt.figure(1, figsize=(12,6))
    
    # Mercator of World
    m1 = Basemap(projection='merc',
                 llcrnrlat=-60,
                 urcrnrlat=65,
                 llcrnrlon=-180,
                 urcrnrlon=180,
                 lat_ts=0,
                 resolution='c')
    
    m1.fillcontinents(color='#666699',lake_color='#000080') # dark grey land, black lakes
    m1.drawmapboundary(fill_color='#000000')                # black background
    m1.drawcountries(linewidth=0.1, color="w")              # thin white line for country borders
    
    # Plot the data
    mxy = m1(df_events_sample["longitude"].tolist(), df_events_sample["latitude"].tolist())
    m1.scatter(mxy[0], mxy[1], s=3, c="#ff9933", lw=0, alpha=1, zorder=5) # represent mobiles in orange
    
    plt.title("Global view of events")
    plt.show()
    
def plot_corr(corr):
    # Plot corr:
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 11))
    
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1,
                square=True, xticklabels=5, yticklabels=5,
                linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)