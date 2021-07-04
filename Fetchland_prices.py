###############################################################################
# Programmer: Kyle Schademan
# Date: 3/28/2020
# Description: Plot of Fetchland prices over time
###############################################################################

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import os

def ShowMeWhatYouGot():
    '''
    combines above functions to plot
    '''
    Dates = []
    
    for i in range(0,50):
        n = float(i)/40
        Dates = np.append(Dates, 2020+n)

    Data = FetchpriceR()
    
    #code that works
    #costVtime(Data[0], Dates)
    
    costVtime(Data[0], Data[1])
    
def FetchpriceR():
    '''
    reads the prices from a txt file and returns the information as an array
    '''
    
    #open our txt file to read the fetchland prices and dates
    filepath = os.path.join('C:/Users/backup/Fetchland_Prices', 'Fetchland_prices.txt')
    if not os.path.exists('C:/Users/backup/Fetchland_Prices'):
        os.makedirs('C:/Users/backup/Fetchland_Prices')
    f = open(filepath, 'r')
    
    #create a storage array for the prices of fetchlands and dates
    Fetchlands = [[],[],[],[],[],[],[],[],[],[]]
    Dates = []
    
    #iterator
    i=0
    #record values from our file into arrays
    for x in f:
        if(i==10):
            Dates = np.append(Dates, x)
        else:
            Fetchlands[i] = np.append(Fetchlands[i], x)
        i=i+1
      
    #iterator
    i=0
    #convert values in our arrays into floats and dates
    for x in Fetchlands:
        Fetchlands[i] = np.fromstring(Fetchlands[i], dtype=float, sep=",")
        if not isinstance(Fetchlands[i][-1], float):
            Fetchlands[i] = Fetchlands[i][:-1]
        if (Fetchlands[i][-1] == -1):
            Fetchlands[i] = Fetchlands[i][:-1]
        i=i+1
        
    Dates = Dates[0].split(",")
    Dates = Dates[:-1]
    
    
    #create storage for date object
    date_obj = []
    for j in Dates:
        j = np.fromstring(j, dtype=int, sep="-")
        date_obj = np.append(date_obj, dt.date(j[0],j[1],j[2])) 
    
    #return values
    return(Fetchlands,date_obj)
    
    
def costVtime(cost, dates):
    '''
    pulls and assigns data from provided arrays and plots them
    '''
    
    #data storage
    # Arid_Mesa = []          #0
    # Bloodstained_Mire = []  #1
    # Flooded_Strand = []     #2
    # Marsh_Flats = []        #3
    # Misty_Rainforest = []   #4
    # Polluted_Delta = []     #5
    # Scalding_Tarn = []      #6
    # Verdent_Catacombs = []  #7
    # Windswept_Heath = []    #8
    # Wooded_Foothills = []   #9
    
    #assign data from cost array
    Arid_Mesa = cost[0]          #0
    Bloodstained_Mire = cost[1]  #1
    Flooded_Strand = cost[2]     #2
    Marsh_Flats = cost[3]        #3
    Misty_Rainforest = cost[4]   #4
    Polluted_Delta = cost[5]     #5
    Scalding_Tarn = cost[6]      #6
    Verdent_Catacombs = cost[7]  #7
    Windswept_Heath = cost[8]    #8
    Wooded_Foothills = cost[9]   #9
    
    #plot controls
    fig, ax = plt.subplots(1, 1, figsize=(12, 14))
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2)) 
    plt.gcf().autofmt_xdate() 
      
    ax.set_xlim(dates[0],dates[-1])
    ax.set_ylim(0,150)
    
    #ax.set_xticks(range(2020,2021))
    #ax.set_yticks(range(0,150,5)) 
    
    #create an indexing variable
    n = 0
    #plot the costs of the fetchlands against the date
    for j in dates:
        date = j
        if(j == dates[-1]):
            ax.plot(date, Arid_Mesa[n], 'r+',label = 'Arid Mesa'
                                                + ' ' + str(Arid_Mesa[-1]))      #0
            ax.plot(date, Bloodstained_Mire[n], 'rx',label = 'Bloodstained Mire'
                                        + ' ' + str(Bloodstained_Mire[-1]))      #1
            ax.plot(date, Flooded_Strand[n], 'b+',label = 'Flooded Strand'
                                           + ' ' + str(Flooded_Strand[-1]))      #2
            ax.plot(date, Marsh_Flats[n], 'g+',label = 'Marsh Flats'
                                              + ' ' + str(Marsh_Flats[-1]))      #3
            ax.plot(date, Misty_Rainforest[n], 'gx',label = 'Misty Rainforest'
                                         + ' ' + str(Misty_Rainforest[-1]))      #4
            ax.plot(date, Polluted_Delta[n], 'bx',label = 'Polluted Delta'
                                           + ' ' + str(Polluted_Delta[-1]))      #5 
            ax.plot(date, Scalding_Tarn[n], 'ro',label = 'Scalding Tarn'
                                            + ' ' + str(Scalding_Tarn[-1]))      #6
            ax.plot(date, Verdent_Catacombs[n], 'yo',label = 'Verdent Catacombs'
                                        + ' ' + str(Verdent_Catacombs[-1]))      #7
            ax.plot(date, Windswept_Heath[n], 'go',label = 'Windswept Heath'
                                          + ' ' + str(Windswept_Heath[-1]))      #8
            ax.plot(date, Wooded_Foothills[n], 'bo',label = 'Wooded Foothills'
                                         + ' ' + str(Wooded_Foothills[-1]))      #9
        else:
            ax.plot(date, Arid_Mesa[n], 'r+')         #0
            ax.plot(date, Bloodstained_Mire[n], 'rx') #1
            ax.plot(date, Flooded_Strand[n], 'b+')    #2
            ax.plot(date, Marsh_Flats[n], 'g+')       #3
            ax.plot(date, Misty_Rainforest[n], 'gx')  #4
            ax.plot(date, Polluted_Delta[n], 'bx')    #5 
            ax.plot(date, Scalding_Tarn[n], 'ro')     #6
            ax.plot(date, Verdent_Catacombs[n], 'yo') #7
            ax.plot(date, Windswept_Heath[n], 'go')   #8
            ax.plot(date, Wooded_Foothills[n], 'bo')  #9
        n = n+1     
    
    #plot labels
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title('Fetchland Prices\nOver time')
    plt.legend(loc = 'upper left')
    
    #show the plot
    plt.show()
    

          
             
                   