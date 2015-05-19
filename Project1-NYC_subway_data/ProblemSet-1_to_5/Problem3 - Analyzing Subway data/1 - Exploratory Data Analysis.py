Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    turnstile_weather1 = turnstile_weather[(turnstile_weather["rain"]==1)] # hourly entries when it is raining
    turnstile_weather2 = turnstile_weather[(turnstile_weather["rain"]==0)] # hourly entries when it is not raining
    turnstile_weather1['ENTRIESn_hourly'].hist()
    turnstile_weather2['ENTRIESn_hourly'].hist()
    plt.xlabel("ENTRIESn_hourly")  #set x-axis label of figure
    plt.ylabel("Frequency")   #set y-axis label of figure
    plt.title("Histogram of ENTRIESn_hourly")  #set title of figure
    plt.legend(["Rain", "No Rain"]) #set legend of figure
    return plt

