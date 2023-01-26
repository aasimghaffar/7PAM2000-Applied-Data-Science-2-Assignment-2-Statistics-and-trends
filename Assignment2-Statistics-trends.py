#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Created January 2023
# @author: Aasim Ghaffar
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats
import seaborn as sns

# this is function for to read and return data
def read_data(name):
    '''
    this function read data file in csv and then preprocessing start then it return country as column and year as column
    and also return original data
    '''
    
    # Read excel file and set variables
    df        = pd.read_excel(name)
    years     = df.head(0)   
    years     = years.drop(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    countries = df.drop(['Country Code', 'Indicator Code'], axis = 1)
    
    # Populate Data
    print(np.array(countries.head))
    print(years.head)
    print(years.info())
    print(countries.info())
    print(df.info())
    print(countries.mean())
    
    return years.T, countries, df

# this function help to get indicator data
def get_indicator_data(indicator, data):
    '''
    this function extract the particular indicator form world bank data and then return it
    '''
    
    return data[data['Indicator Name']==indicator]

# this function take data and country as parameter
def country_data(data, country):
    '''
    this function extract the data of specific country from indicator data and return it
    '''
    
    # get country data from data
    country_data = data[data['Country Name']==country]
    return country_data.drop(['Country Name','Indicator Name'], axis = 1)

# this function show graph line and take year as parameter
def line_graph(years, data, indicator_name):
    '''
    this function plot line graph for total population and power consumption of specific countries 
    '''
    
    # Defining countires
    pak        = country_data(data, "Pakistan")
    ind        = country_data(data, "India")
    china      = country_data(data, "China")
    srilanka   = country_data(data, "Sri Lanka")
    albania    = country_data(data, "Albania")
    spain      = country_data(data, "Spain")
    bangladesh = country_data(data, "Bangladesh")
    
    # Ploting data of these countries
    plt.plot(pd.to_numeric(years.index), pak.iloc[0].to_numpy(), label = "Pakistan", linestyle = "-.")
    plt.plot(pd.to_numeric(years.index), ind.iloc[0].to_numpy(), label = "India", linestyle = "-.")
    plt.plot(pd.to_numeric(years.index), china.iloc[0].to_numpy(), label = "China", linestyle = "-.")
    plt.plot(pd.to_numeric(years.index), srilanka.iloc[0].to_numpy(), label = "SriLanka", linestyle = "-.")
    plt.plot(pd.to_numeric(years.index), bangladesh.iloc[0].to_numpy(), label = "Bangladesh", linestyle = "-.")
    plt.plot(pd.to_numeric(years.index), spain.iloc[0].to_numpy(), label = "Spain", linestyle = "-.")
    plt.plot(pd.to_numeric(years.index), albania.iloc[0].to_numpy(), label = "Albania", linestyle = "-.")
    
    # adding title
    plt.title(indicator_name)
    
    # adding xlabel
    plt.xlabel('Years')
    
    # adding y label
    plt.ylabel('values')
    
    # adding legend
    plt.legend()
    
    # Show graph
    plt.show()

# this function olot bar graph and take year name and color as paramtere
def barplot(indicator_forest, year, name, colors = None, total_width = 0.8, single_width = 1, legend = True):
     '''
     this function plot bar graph of selected countries for last five year of carbon emission and forest area
     '''
     
     # defining seprate dataframe to show barplot
     pak        = country_data(indicator_forest, "Pakistan")
     ind        = country_data(indicator_forest, "India")
     china      = country_data(indicator_forest,"China")
     srilanka   = country_data(indicator_forest, "Sri Lanka")
     albania    = country_data(indicator_forest, "Albania")
     spain      = country_data(indicator_forest, "Spain")
     bangladesh = country_data(indicator_forest, "Bangladesh")
     
     # adding data to list from dataframes
     data = [
            ['2015', pak['2015'].iloc[0], ind['2015'].iloc[0], china['2015'].iloc[0], srilanka['2015'].iloc[0], spain['2015'].iloc[0], albania['2015'].iloc[0], bangladesh['2015'].iloc[0]],
            ['2016', pak['2016'].iloc[0], ind['2016'].iloc[0], china['2016'].iloc[0], srilanka['2016'].iloc[0], spain['2016'].iloc[0], albania['2016'].iloc[0], bangladesh['2015'].iloc[0]],
            ['2017', pak['2017'].iloc[0], ind['2017'].iloc[0], china['2017'].iloc[0], srilanka['2017'].iloc[0], spain['2017'].iloc[0], albania['2017'].iloc[0], bangladesh['2015'].iloc[0]],
            ['2018', pak['2018'].iloc[0], ind['2018'].iloc[0], china['2018'].iloc[0], srilanka['2018'].iloc[0], spain['2018'].iloc[0], albania['2018'].iloc[0], bangladesh['2015'].iloc[0]],
            ['2019', pak['2019'].iloc[0], ind['2019'].iloc[0], china['2019'].iloc[0], srilanka['2019'].iloc[0], spain['2019'].iloc[0], albania['2019'].iloc[0], bangladesh['2015'].iloc[0]],
         ]
     
     # adding column names
     df = pd.DataFrame(data,columns=["Years", "Pakistan", "India", "China", "SriLanka", "Spain", "Albania", "Bangladesh"])
     
     # adding barplot
     df.plot(x = "Years", y = ["Pakistan", "India", "China", "SriLanka", "Spain", "Albania", "Bangladesh"], kind = "bar", figsize = (9, 8), title = name)

     # Show barplot
     plt.show()

# table function show table of countries with year 2000,2015,2020
def table(countries):
    '''
    this function show table of specific countries fro access to electricity percentage of population
    '''
    
    k          = countries[countries['Country Name']=='Pakistan']
    pak        = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    k          = countries[countries['Country Name']=='India']
    ind        = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    k          = countries[countries['Country Name']=='China']
    chi        = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    k          = countries[countries['Country Name']=='Sri Lanka']
    sri        = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    k          = countries[countries['Country Name']=='Albania']
    albania    = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    k          = countries[countries['Country Name']=='Bangladesh']
    bangladesh = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    k          = countries[countries['Country Name']=='Spain']
    spain      = k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    # showing and ploting the graph
    fig, ax    = plt.subplots()
    
    #create values for table
    table_data = [
        ["Countries", 2000, 2015, 2020],
        ["Pakistan", pak.T['2000'].iloc[0], pak.T["2015"].iloc[0], pak.T["2020"].iloc[0]],
        ["India", ind.T['2000'].iloc[0], ind.T["2015"].iloc[0], ind.T["2020"].iloc[0]],
        ["China", chi.T['2000'].iloc[0], chi.T["2015"].iloc[0], chi.T["2020"].iloc[0]],
        ["Spain", spain.T['2000'].iloc[0], spain.T["2015"].iloc[0], spain.T["2020"].iloc[0]],
        ["Albania", albania.T['2000'].iloc[0], albania.T["2015"].iloc[0], albania.T["2020"].iloc[0]],
        ["Bangladesh", bangladesh.T['2000'].iloc[0], bangladesh.T["2015"].iloc[0], bangladesh.T["2020"].iloc[0]],
        ["Sri Lanka", sri.T['2000'].iloc[0], sri.T["2015"].iloc[0], sri.T["2020"].iloc[0]]
    ]
    
    #create table
    table = ax.table(cellText = table_data, loc = 'center')
    
    #modify table
    table.set_fontsize(14)
    
    table.scale(4, 8)
    
    ax.axis('off')
    
    #display table
    plt.show()

def heatmap(data, name):
    '''
    this function show heatmap graph to show correlation between different indicators that are causing the global warming
    '''
    
    # Get country specific data
    k=data[data['Country Name']==name]
    
    # define empty dataframe
    indicator_data = pd.DataFrame()
    
    # get Access to electricity (% of population) indicator
    indicator_data['Access to electricity (% of population)']=k[k['Indicator Name']=="Access to electricity (% of population)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    # get Access to CO2 emissions (kt) indicator
    indicator_data['CO2 emissions (kt)']=k[k['Indicator Name']=="CO2 emissions (kt)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    # get Access to Electric power consumption (kWh per capita) indicator
    indicator_data['Electric power consumption (kWh per capita)']=k[k['Indicator Name']=="Electric power consumption (kWh per capita)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    # get Access to Forest area (sq. km) indicator
    indicator_data['Forest area (sq. km)']=k[k['Indicator Name']=="Forest area (sq. km)"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    # get Access to Population, total indicator
    indicator_data['Population, total']=k[k['Indicator Name']=="Population, total"].drop(['Country Name', 'Indicator Name'], axis = 1).T
    
    # adding column names
    indicator_data.columns = ['Access to electricity (% of population)', 'CO2 emissions (kt)', 'Electric power consumption (kWh per capita)', 'Forest area (sq. km)', 'Population total']
    
    # reseting index
    indicator_data.reset_index(drop = True, inplace = True)
    
    # ploting the data
    ax = plt.axes()
    
    # use sns to plot heatmap
    rel=sns.heatmap(indicator_data.corr(), cmap="YlGnBu", annot = True, ax = ax);
    
    # adding title
    ax.set_title(name)
    
    # show plot
    plt.show()
        
# Main Function
if __name__ == "__main__":
    
    # Set Variables
    years, countries, original = read_data('data.xls')
    
    # Draw line graph
    indicator_population = get_indicator_data("Population, total", countries)
    line_graph(years, indicator_population, 'Population, total')
    
    # Draw bar plot
    indicator_forest = get_indicator_data("CO2 emissions (kt)", countries)
    barplot(indicator_forest, years, "CO2 emissions (kt)", total_width = .8, single_width = .9)
    
    # Draw bar plot
    indicator_forest = get_indicator_data("Forest area (sq. km)", countries)
    barplot(indicator_forest,years, "Forest area (sq. km)", total_width = .8, single_width = .9)
    
    # Draw line plot
    indicator_population = get_indicator_data("Electric power consumption (kWh per capita)", countries)
    line_graph(years, indicator_population, "Electric power consumption (kWh per capita)")
    
    # Draw table
    table(countries)
    
    # Draw line graph
    indicator_population = get_indicator_data("Access to electricity (% of population)", countries)
    line_graph(years, indicator_population,' Access to electricity (% of population)')
    
    # Draw heatmap
    heatmap(countries,'China')
    heatmap(countries,'Sri Lanka')
    heatmap(countries, 'India')