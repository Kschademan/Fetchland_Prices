###############################################################################
# Programmer: Kyle Schademan
# Date: 3/28/2020
# Description: Plot of Fetchland prices over time
###############################################################################

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import csv

def ShowMeWhatYouGot():
    '''
    combines above functions to plot
    '''
    from datetime import date
    today = date.today().strftime("%Y")
    
    costVtime(Fetchprice(),(2020, 2021, 2022, 2023))

def Fetchprice():
    '''
    returns current prices of the fetchlands
    '''
    
    #create a storage array for the prices of fetchlands
    Fetchlands = [[],[],[],[],[],[],[],[],[],[]]
    
    # with open('Fetchlandprices.txt') as in_file:
    #     print(10)
    
    #append the prices of the fetchlands to the storage array
    Fetchlands[0] = np.append(Fetchlands[0], 27.62)
    Fetchlands[1] = np.append(Fetchlands[1], 16.03)
    Fetchlands[2] = np.append(Fetchlands[2], 33.93)
    Fetchlands[3] = np.append(Fetchlands[3], 31.28)
    Fetchlands[4] = np.append(Fetchlands[4], 62.63)
    Fetchlands[5] = np.append(Fetchlands[5], 15.30)
    Fetchlands[6] = np.append(Fetchlands[6], 56.03)
    Fetchlands[7] = np.append(Fetchlands[7], 48.96)
    Fetchlands[8] = np.append(Fetchlands[8], 8.90)
    Fetchlands[9] = np.append(Fetchlands[9], 14.32)
    
    #append the prices to the fetchlands for the next day
    Fetchlands[0] = np.append(Fetchlands[0], 27.30)
    Fetchlands[1] = np.append(Fetchlands[1], 14.86)
    Fetchlands[2] = np.append(Fetchlands[2], 33.73)
    Fetchlands[3] = np.append(Fetchlands[3], 29.58)
    Fetchlands[4] = np.append(Fetchlands[4], 62.83)
    Fetchlands[5] = np.append(Fetchlands[5], 17.34)
    Fetchlands[6] = np.append(Fetchlands[6], 53.91)
    Fetchlands[7] = np.append(Fetchlands[7], 46.56)
    Fetchlands[8] = np.append(Fetchlands[8], 9.80)
    Fetchlands[9] = np.append(Fetchlands[9], 14.76)
    
    #append the prices to the fetchlands for the next day
    Fetchlands[0] = np.append(Fetchlands[0], 27.90)
    Fetchlands[1] = np.append(Fetchlands[1], 15.95)
    Fetchlands[2] = np.append(Fetchlands[2], 15.59)
    Fetchlands[3] = np.append(Fetchlands[3], 27.87)
    Fetchlands[4] = np.append(Fetchlands[4], 63.02)
    Fetchlands[5] = np.append(Fetchlands[5], 19.04)
    Fetchlands[6] = np.append(Fetchlands[6], 56.40)
    Fetchlands[7] = np.append(Fetchlands[7], 50.33)
    Fetchlands[8] = np.append(Fetchlands[8], 10.65)
    Fetchlands[9] = np.append(Fetchlands[9], 16.12)
    
    #append the prices to the fetchlands for the next day
    Fetchlands[0] = np.append(Fetchlands[0], 30.40)
    Fetchlands[1] = np.append(Fetchlands[1], 17.32)
    Fetchlands[2] = np.append(Fetchlands[2], 15.99)
    Fetchlands[3] = np.append(Fetchlands[3], 30.71)
    Fetchlands[4] = np.append(Fetchlands[4], 67.31)
    Fetchlands[5] = np.append(Fetchlands[5], 20.11)
    Fetchlands[6] = np.append(Fetchlands[6], 60.51)
    Fetchlands[7] = np.append(Fetchlands[7], 54.57)
    Fetchlands[8] = np.append(Fetchlands[8], 11.73)
    Fetchlands[9] = np.append(Fetchlands[9], 17.55)
    
    f = open('Fetchland_prices.txt', 'w')
    for i in range(0,10):
        for j in range(0,4):
            f.write(str(Fetchlands[i][j]))
            f.write(',')
        f.write('\n')
    f.close()
    
    #return the prices of the fetchlands
    return(Fetchlands)
    
    
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
    
    ax.set_xlim(2019.5,2025.5)
    ax.set_ylim(0,100)
    
    ax.set_xticks(range(2020,2025,1))
    ax.set_yticks(range(0,100,5))
    
    #create an indexing variable
    n = 0
    #plot the costs of the fetchlands against the date
    for j in dates:
        date = j
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
    
    #show the plot
    plt.show()
    

          
             
                   