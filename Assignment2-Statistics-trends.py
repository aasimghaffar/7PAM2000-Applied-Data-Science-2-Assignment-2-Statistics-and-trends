#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Created December 2022
# @author: Aasim Ghaffar
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV File
def get_data(name):
    """
    # this function get data from xlsx
    # then store it in data variable and return the data
    """
    
    # read data
    df = pd.read_csv(name, skiprows = 4)
    
    origdata = df.drop([
        'Country Code',
        'Indicator Code'
    ], axis = 1)
    
    countdata = df.drop([
        'Country Code',
        'Indicator Name',
        'Indicator Code'
    ], axis = 1)
    
    yedata = df.drop([
        'Country Name', 
        'Country Code', 
        'Indicator Name', 
        'Indicator Code'
    ], axis = 1).T
    
    yedata.index.name='Years'
    
    # print the data of head
    print(yedata.head)
    print(countdata.head)
    print(origdata.head)
    print(origdata.T)
    
    # return data value of year and column
    return countdata, yedata, origdata

def graph(data, diagram, indicator = '', indicator_name = ''):
    if diagram=="barPlot_1":

        # plot a bar graph (4 countries year 1996 - 2016)
        fdata   = data[data["Indicator Name"] == indicator]
        uk      = fdata[fdata["Country Name"] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1)
        latvia  = fdata[fdata["Country Name"] == "Brazil"]
        morocco = fdata[fdata["Country Name"] == "Peru"]
        mexico  = fdata[fdata["Country Name"] == "Sweden"]    
        index   = ['1996', '2000', '2004', '2008', '2012', '2016']
        
        df = pd.DataFrame({
            'Brazil': [
                latvia['1996'].iloc[0], 
                latvia['2000'].iloc[0], 
                latvia['2004'].iloc[0],
                latvia['2008'].iloc[0],
                latvia['2012'].iloc[0],
                latvia['2016'].iloc[0]
            ],
            'Peru': [
                morocco['1996'].iloc[0],
                morocco['2000'].iloc[0],
                morocco['2004'].iloc[0],
                morocco['2008'].iloc[0],
                morocco['2012'].iloc[0],
                morocco['2016'].iloc[0]
            ],
            'Zambia': [
                uk['1996'].iloc[0],
                uk['2000'].iloc[0],
                uk['2004'].iloc[0],
                uk['2008'].iloc[0],
                uk['2012'].iloc[0],
                uk['2016'].iloc[0]
            ],
            'Sweden': [
                mexico['1996'].iloc[0],
                mexico['2000'].iloc[0],
                mexico['2004'].iloc[0],
                mexico['2008'].iloc[0],
                mexico['2012'].iloc[0],
                mexico['2016'].iloc[0]
            ],
        }, index = index)
        
        # ploting bar graph
        ax = df.plot.barh(title = indicator_name)
        
        # Generate Chart Image
        plt.savefig('bar1.png')
        
        # ploting bar graph show
        plt.show()
    elif diagram=="barPlot_2":
        
        # plot a bar graph (4 countries year 1996 - 2016)    
        fdata   = data[data["Indicator Name"] == indicator]
        uk      = fdata[fdata["Country Name"] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1)
        latvia  = fdata[fdata["Country Name"] == "Brazil"]    
        morocco = fdata[fdata["Country Name"] == "Peru"]
        mexico = fdata[fdata["Country Name"] == "Sweden"]
        index = ['1996', '2000', '2004', '2008', '2012', '2016']
        
        df = pd.DataFrame({
            'Brazil': [
                latvia['1996'].iloc[0],
                latvia['2000'].iloc[0],
                latvia['2004'].iloc[0],
                latvia['2008'].iloc[0],
                latvia['2012'].iloc[0],
                latvia['2016'].iloc[0]
            ],
            'Peru': [
                morocco['1996'].iloc[0],
                morocco['2000'].iloc[0],
                morocco['2004'].iloc[0],
                morocco['2008'].iloc[0],
                morocco['2012'].iloc[0],
                morocco['2016'].iloc[0]
            ],
            'Zambia': [
                uk['1996'].iloc[0],
                uk['2000'].iloc[0],
                uk['2004'].iloc[0],
                uk['2008'].iloc[0],
                uk['2012'].iloc[0],
                uk['2016'].iloc[0]
            ],
            'Sweden': [
                mexico['1996'].iloc[0],
                mexico['2000'].iloc[0],
                mexico['2004'].iloc[0],
                mexico['2008'].iloc[0],
                mexico['2012'].iloc[0],
                mexico['2016'].iloc[0]
            ],
        }, index = index)
        
        # ploting bar graph
        ax = df.plot.barh(title = indicator_name)
        
        # Generate Chart Image
        plt.savefig('bar2.png')
        
        # ploting bar graph Show
        plt.show()
    elif diagram=="lineGraph_1":
        
        # plot a Lie graph (Specific 4 Countries)
        fdata   = data[data["Indicator Name"] == indicator]
        uk      = fdata[fdata["Country Name"] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1)
        latvia  = fdata[fdata["Country Name"] == "Brazil"].drop(['Country Name', 'Indicator Name'], axis = 1)
        morocco = fdata[fdata["Country Name"] == "Peru"].drop(['Country Name', 'Indicator Name'], axis = 1)
        mexico  = fdata[fdata["Country Name"] == "Sweden"].drop(['Country Name', 'Indicator Name'], axis = 1)
      
        # Year
        year = data.drop(['Country Name', 'Indicator Name'], axis = 1).T.index
        
        print(year)
        
        # plotting the points 
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), uk.iloc[0].dropna().to_numpy(), label = "Zambia", linestyle = "-.")
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), latvia.iloc[0].dropna().to_numpy(), label = "Brazil", linestyle = "-.")
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), morocco.iloc[0].dropna().to_numpy(), label = "Peru", linestyle = "-.")
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), mexico.iloc[0].dropna().to_numpy(), label = "Sweden", linestyle = "-.")    
          
        # x axis Label
        plt.xlabel('year')

        # y axis Lable
        plt.ylabel('data')
        plt.legend()

        # Lable title
        plt.title(indicator_name)
          
        # Generate Chart Image
        plt.savefig('line1.png')
        
        # ploting Lie graph show
        plt.show()
    elif diagram=="lineGraph_2":
        # plot a Lie graph (Specific 4 Countries)
        fdata   = data[data["Indicator Name"] == indicator]    
        uk      = fdata[fdata["Country Name"] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1)
        latvia  = fdata[fdata["Country Name"] == "Brazil"].drop(['Country Name', 'Indicator Name'], axis = 1)
        morocco = fdata[fdata["Country Name"] == "Peru"].drop(['Country Name', 'Indicator Name'], axis = 1)
        mexico  = fdata[fdata["Country Name"] == "Sweden"].drop(['Country Name', 'Indicator Name'], axis = 1)
      
        # year
        year = data.drop(['Country Name', 'Indicator Name'], axis = 1).T.index
        
        print(year)
        
        # plotting points 
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), uk.iloc[0].dropna().to_numpy(), label = "Zambia", linestyle = "-.")
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), latvia.iloc[0].dropna().to_numpy(), label = "Brazil", linestyle = "-.")
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), morocco.iloc[0].dropna().to_numpy(), label = "Peru", linestyle = "-.")
        plt.plot(pd.to_numeric(year[0:60].to_numpy()), mexico.iloc[0].dropna().to_numpy(), label = "Sweden", linestyle = "-.")
              
        # x axis Label
        plt.xlabel('year')
    
        # y axis Lable
        plt.ylabel('data')
        plt.legend()
    
        # Lable title
        plt.title(indicator_name)
          
        # Generate Chart Image
        plt.savefig('line2.png')
        
        # ploting bar graph show
        plt.show()
    elif diagram=="France":
        
        # plot a heatmap (Indicator)
        fdata   = pd.DataFrame()
        bradata = data[data["Indicator Name"] == "Methane emissions (kt of CO2 equivalent)"]
        bradata = bradata[bradata['Country Name']=="Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata["Methane emissions (kt of CO2 equivalent)"] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Arable land (% of land area)']
        bradata = bradata[bradata['Country Name'] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Arable land (% of land area)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Population growth (annual %)']
        bradata = bradata[bradata['Country Name'] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Population growth (annual %)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Agricultural land (sq. km)']
        bradata = bradata[bradata['Country Name'] == "Zambia"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Agricultural land (sq. km)'] = bradata.iloc[0]
        ax      = plt.axes()
            
        # Heatmap
        heatmap = sns.heatmap(fdata.corr(), cmap = "tab10", annot = True, ax = ax)
        
        # Lable title
        ax.set_title('Zambia')
        
        # Generate Chart Image
        plt.savefig('heat1.png')
        
        # ploting Heatmap graph show
        plt.show()
    elif diagram=="Peru":
        
        # plot a heatmap (Indicator)
        fdata   = pd.DataFrame()
        bradata = data[data["Indicator Name"] == "Methane emissions (kt of CO2 equivalent)"]
        bradata = bradata[bradata['Country Name'] == "Brazil"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata["Methane emissions (kt of CO2 equivalent)"] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Arable land (% of land area)']
        bradata = bradata[bradata['Country Name'] == "Brazil"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
            
        fdata['Arable land (% of land area)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Population growth (annual %)']
        bradata = bradata[bradata['Country Name'] == "Brazil"].drop(['Country Name','Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Population growth (annual %)'] = bradata.iloc[0]    
        bradata = data[data["Indicator Name"] == 'Agricultural land (sq. km)']
        bradata = bradata[bradata['Country Name'] == "Brazil"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Agricultural land (sq. km)'] = bradata.iloc[0]
        ax = plt.axes()
            
        # Heatmap
        heatmap = sns.heatmap(fdata.corr(), cmap = "tab10", annot = True, ax = ax)
        
        # Lable title
        ax.set_title('Brazil')
        
        # Generate Chart Image
        plt.savefig('heat2.png')
        
        # ploting Heatmap graph show
        plt.show()
    elif diagram=="Zambia":
        
        # plot a heatmap (Indicator)
        fdata   = pd.DataFrame()
        bradata = data[data["Indicator Name"] == "Methane emissions (kt of CO2 equivalent)"]
        bradata = bradata[bradata['Country Name'] == "Peru"].drop(['Country Name','Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
            
        fdata["Methane emissions (kt of CO2 equivalent)"] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Arable land (% of land area)']
        bradata = bradata[bradata['Country Name'] == "Peru"].drop(['Country Name','Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Arable land (% of land area)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Population growth (annual %)']
        bradata = bradata[bradata['Country Name'] == "Peru"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Population growth (annual %)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Agricultural land (sq. km)']
        bradata = bradata[bradata['Country Name'] == "Peru"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Agricultural land (sq. km)'] = bradata.iloc[0]
        ax = plt.axes()
            
        # Heatmap
        heatmap = sns.heatmap(fdata.corr(), cmap="tab10", annot=True,ax=ax)
        
        # Lable title
        ax.set_title('Peru')    
        
        # Generate Chart Image
        plt.savefig('heat3.png')
        
        # ploting Heatmap graph show
        plt.show()
    elif diagram=="Sweden":
        # plot a heatmap (Indicator)
        fdata   = pd.DataFrame()
        bradata = data[data["Indicator Name"] == "Methane emissions (kt of CO2 equivalent)"]
        bradata = bradata[bradata['Country Name'] == "Sweden"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
            
        fdata["Methane emissions (kt of CO2 equivalent)"] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Arable land (% of land area)']
        bradata = bradata[bradata['Country Name'] == "Sweden"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
            
        fdata['Arable land (% of land area)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Population growth (annual %)']
        bradata = bradata[bradata['Country Name'] == "Sweden"].drop(['Country Name', 'Indicator Name'], axis = 1).T        
        bradata = bradata.dropna().T    
        
        fdata['Population growth (annual %)'] = bradata.iloc[0]
        bradata = data[data["Indicator Name"] == 'Agricultural land (sq. km)'] 
        bradata = bradata[bradata['Country Name'] == "Sweden"].drop(['Country Name', 'Indicator Name'], axis = 1).T
        bradata = bradata.dropna().T
        
        fdata['Agricultural land (sq. km)'] = bradata.iloc[0]
        ax = plt.axes()
            
        # Heatmap
        heatmap = sns.heatmap(fdata.corr(), cmap = "tab10", annot = True, ax = ax)
        
        # Lable title
        ax.set_title('Sweden')    
        
        # Generate Chart Image
        plt.savefig('heat4.png')
        
        # ploting Heatmap graph show
        plt.show()

# Get Data   
coundata, yedata, origdata = get_data("data.csv")

# Calling Function
graph(origdata, 'barPlot_1', 'Methane emissions (kt of CO2 equivalent)', 'Methane emissions (kt of CO2 equivalent)')
graph(origdata, 'barPlot_2', 'Population growth (annual %)', 'Population growth (annual %)')
graph(origdata, 'lineGraph_1', 'Arable land (% of land area)', 'Arable land (% of land area)')
graph(origdata, 'lineGraph_2', 'Agricultural land (sq. km)', 'Agricultural land (sq. km)')
graph(origdata, 'France')
graph(origdata, 'Peru')
graph(origdata, 'Zambia')
graph(origdata, 'Sweden')