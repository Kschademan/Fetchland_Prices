#import libraries
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
    

def FetchpriceW():
    '''
    returns current prices of the fetchlands and the dates those were recorded
    '''
    
    #create a storage array for the prices of fetchlands
    Fetchlands = [[],[],[],[],[],[],[],[],[],[],[]]
    
    #append the prices of the fetchlands to the storage array//1
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
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,3,29))
    
    #append the prices to the fetchlands for the next day//2
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
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,4,5))
    
    #append the prices to the fetchlands for the next day//3
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
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,4,12))
    
    #append the prices to the fetchlands for the next day//4
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
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,4,19))
    
    #append the prices to the fetchlands for the next day//5
    Fetchlands[0] = np.append(Fetchlands[0], 30.21)
    Fetchlands[1] = np.append(Fetchlands[1], 19.37)
    Fetchlands[2] = np.append(Fetchlands[2], 16.39)
    Fetchlands[3] = np.append(Fetchlands[3], 33.32)
    Fetchlands[4] = np.append(Fetchlands[4], 73.43)
    Fetchlands[5] = np.append(Fetchlands[5], 22.70)
    Fetchlands[6] = np.append(Fetchlands[6], 63.25)
    Fetchlands[7] = np.append(Fetchlands[7], 58.11)
    Fetchlands[8] = np.append(Fetchlands[8], 12.23)
    Fetchlands[9] = np.append(Fetchlands[9], 18.70)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,4,26))
    
    #append the prices to the fetchlands for the next day//6
    Fetchlands[0] = np.append(Fetchlands[0], 30.39)
    Fetchlands[1] = np.append(Fetchlands[1], 20.37)
    Fetchlands[2] = np.append(Fetchlands[2], 17.33)
    Fetchlands[3] = np.append(Fetchlands[3], 35.20)
    Fetchlands[4] = np.append(Fetchlands[4], 77.74)
    Fetchlands[5] = np.append(Fetchlands[5], 21.83)
    Fetchlands[6] = np.append(Fetchlands[6], 63.88)
    Fetchlands[7] = np.append(Fetchlands[7], 62.55)
    Fetchlands[8] = np.append(Fetchlands[8], 12.08)
    Fetchlands[9] = np.append(Fetchlands[9], 19.54)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,5,3))
    
    #append the prices to the fetchlands for the next day(5/10/12020)//7
    Fetchlands[0] = np.append(Fetchlands[0], 32.97)
    Fetchlands[1] = np.append(Fetchlands[1], 21.15)
    Fetchlands[2] = np.append(Fetchlands[2], 18.42)
    Fetchlands[3] = np.append(Fetchlands[3], 37.82)
    Fetchlands[4] = np.append(Fetchlands[4], 85.39)
    Fetchlands[5] = np.append(Fetchlands[5], 23.85)
    Fetchlands[6] = np.append(Fetchlands[6], 66.95)
    Fetchlands[7] = np.append(Fetchlands[7], 67.10)
    Fetchlands[8] = np.append(Fetchlands[8], 13.36)
    Fetchlands[9] = np.append(Fetchlands[9], 21.65)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,5,10))
    
    #append the prices to the fetchlands for the next day(5/17/12020)//8
    Fetchlands[0] = np.append(Fetchlands[0], 35.11)
    Fetchlands[1] = np.append(Fetchlands[1], 21.91)
    Fetchlands[2] = np.append(Fetchlands[2], 19.83)
    Fetchlands[3] = np.append(Fetchlands[3], 38.82)
    Fetchlands[4] = np.append(Fetchlands[4], 87.15)
    Fetchlands[5] = np.append(Fetchlands[5], 24.14)
    Fetchlands[6] = np.append(Fetchlands[6], 68.92)
    Fetchlands[7] = np.append(Fetchlands[7], 71.37)
    Fetchlands[8] = np.append(Fetchlands[8], 13.66)
    Fetchlands[9] = np.append(Fetchlands[9], 23.06)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,5,17))
    
    #append the prices to the fetchlands for the next day(5/24/12020)//9
    Fetchlands[0] = np.append(Fetchlands[0], 38.40)
    Fetchlands[1] = np.append(Fetchlands[1], 23.71)
    Fetchlands[2] = np.append(Fetchlands[2], 20.66)
    Fetchlands[3] = np.append(Fetchlands[3], 41.20)
    Fetchlands[4] = np.append(Fetchlands[4], 86.41)
    Fetchlands[5] = np.append(Fetchlands[5], 26.16)
    Fetchlands[6] = np.append(Fetchlands[6], 54.33)
    Fetchlands[7] = np.append(Fetchlands[7], 74.77)
    Fetchlands[8] = np.append(Fetchlands[8], 15.50)
    Fetchlands[9] = np.append(Fetchlands[9], 23.81)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,5,24))
    
    #append the prices to the fetchlands for the next day(5/31/12020)//10
    Fetchlands[0] = np.append(Fetchlands[0], 38.97)
    Fetchlands[1] = np.append(Fetchlands[1], 24.62)
    Fetchlands[2] = np.append(Fetchlands[2], 20.39)
    Fetchlands[3] = np.append(Fetchlands[3], 41.65)
    Fetchlands[4] = np.append(Fetchlands[4], 89.03)
    Fetchlands[5] = np.append(Fetchlands[5], 26.39)
    Fetchlands[6] = np.append(Fetchlands[6], 61.10)
    Fetchlands[7] = np.append(Fetchlands[7], 73.22)
    Fetchlands[8] = np.append(Fetchlands[8], 15.89)
    Fetchlands[9] = np.append(Fetchlands[9], 25.67)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,5,31))
    
    #append the prices to the fetchlands for the next day(6/7/12020)//11
    Fetchlands[0] = np.append(Fetchlands[0], 39.51)
    Fetchlands[1] = np.append(Fetchlands[1], 25.18)
    Fetchlands[2] = np.append(Fetchlands[2], 20.63)
    Fetchlands[3] = np.append(Fetchlands[3], 41.67)
    Fetchlands[4] = np.append(Fetchlands[4], 88.89)
    Fetchlands[5] = np.append(Fetchlands[5], 28.20)
    Fetchlands[6] = np.append(Fetchlands[6], 65.47)
    Fetchlands[7] = np.append(Fetchlands[7], 74.94)
    Fetchlands[8] = np.append(Fetchlands[8], 15.81)
    Fetchlands[9] = np.append(Fetchlands[9], 25.24)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,6,7))
    
    #append the prices to the fetchlands for the next day(6/14/12020)//12
    Fetchlands[0] = np.append(Fetchlands[0], 40.54)
    Fetchlands[1] = np.append(Fetchlands[1], 23.85)
    Fetchlands[2] = np.append(Fetchlands[2], 20.66)
    Fetchlands[3] = np.append(Fetchlands[3], 38.03)
    Fetchlands[4] = np.append(Fetchlands[4], 88.32)
    Fetchlands[5] = np.append(Fetchlands[5], 27.03)
    Fetchlands[6] = np.append(Fetchlands[6], 72.76)
    Fetchlands[7] = np.append(Fetchlands[7], 59.01)
    Fetchlands[8] = np.append(Fetchlands[8], 16.33)
    Fetchlands[9] = np.append(Fetchlands[9], 25.28)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,6,14))
    
    #append the prices to the fetchlands for the next day(6/28/12020)//13
    Fetchlands[0] = np.append(Fetchlands[0], 35.95)
    Fetchlands[1] = np.append(Fetchlands[1], 23.47)
    Fetchlands[2] = np.append(Fetchlands[2], 20.42)
    Fetchlands[3] = np.append(Fetchlands[3], 36.44)
    Fetchlands[4] = np.append(Fetchlands[4], 78.83)
    Fetchlands[5] = np.append(Fetchlands[5], 26.34)
    Fetchlands[6] = np.append(Fetchlands[6], 67.47)
    Fetchlands[7] = np.append(Fetchlands[7], 64.35)
    Fetchlands[8] = np.append(Fetchlands[8], 16.89)
    Fetchlands[9] = np.append(Fetchlands[9], 25.14)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,6,28))
    
    #append the prices to the fetchlands for the next day(7/12/12020)//14
    Fetchlands[0] = np.append(Fetchlands[0], 38.25)
    Fetchlands[1] = np.append(Fetchlands[1], 24.61)
    Fetchlands[2] = np.append(Fetchlands[2], 19.30)
    Fetchlands[3] = np.append(Fetchlands[3], 37.73)
    Fetchlands[4] = np.append(Fetchlands[4], 71.29)
    Fetchlands[5] = np.append(Fetchlands[5], 24.42)
    Fetchlands[6] = np.append(Fetchlands[6], 60.42)
    Fetchlands[7] = np.append(Fetchlands[7], 61.20)
    Fetchlands[8] = np.append(Fetchlands[8], 16.78)
    Fetchlands[9] = np.append(Fetchlands[9], 23.73)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,7,12))
    
    #append the prices to the fetchlands for the next day(7/19/12020)//15
    Fetchlands[0] = np.append(Fetchlands[0], 35.91)
    Fetchlands[1] = np.append(Fetchlands[1], 23.79)
    Fetchlands[2] = np.append(Fetchlands[2], 18.71)
    Fetchlands[3] = np.append(Fetchlands[3], 38.37)
    Fetchlands[4] = np.append(Fetchlands[4], 71.24)
    Fetchlands[5] = np.append(Fetchlands[5], 24.50)
    Fetchlands[6] = np.append(Fetchlands[6], 63.42)
    Fetchlands[7] = np.append(Fetchlands[7], 60.42)
    Fetchlands[8] = np.append(Fetchlands[8], 15.88)
    Fetchlands[9] = np.append(Fetchlands[9], 21.37)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,7,19))
    
    #append the prices to the fetchlands for the next day(8/2/12020)//16
    Fetchlands[0] = np.append(Fetchlands[0], 35.31)
    Fetchlands[1] = np.append(Fetchlands[1], 22.53)
    Fetchlands[2] = np.append(Fetchlands[2], 19.12)
    Fetchlands[3] = np.append(Fetchlands[3], 36.38)
    Fetchlands[4] = np.append(Fetchlands[4], 69.17)
    Fetchlands[5] = np.append(Fetchlands[5], 24.36)
    Fetchlands[6] = np.append(Fetchlands[6], 63.15)
    Fetchlands[7] = np.append(Fetchlands[7], 58.87)
    Fetchlands[8] = np.append(Fetchlands[8], 14.90)
    Fetchlands[9] = np.append(Fetchlands[9], 24.29)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,8,2))
    
    #append the prices to the fetchlands for the next day(8/16/12020)//17
    Fetchlands[0] = np.append(Fetchlands[0], 34.96)
    Fetchlands[1] = np.append(Fetchlands[1], 23.80)
    Fetchlands[2] = np.append(Fetchlands[2], 18.85)
    Fetchlands[3] = np.append(Fetchlands[3], 34.65)
    Fetchlands[4] = np.append(Fetchlands[4], 71.34)
    Fetchlands[5] = np.append(Fetchlands[5], 26.49)
    Fetchlands[6] = np.append(Fetchlands[6], 59.88)
    Fetchlands[7] = np.append(Fetchlands[7], 60.29)
    Fetchlands[8] = np.append(Fetchlands[8], 15.26)
    Fetchlands[9] = np.append(Fetchlands[9], 24.98)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,8,16))
    
    #append the prices to the fetchlands for the next day(9/2/12020)//18
    Fetchlands[0] = np.append(Fetchlands[0], 30.70)
    Fetchlands[1] = np.append(Fetchlands[1], 24.78)
    Fetchlands[2] = np.append(Fetchlands[2], 19.53)
    Fetchlands[3] = np.append(Fetchlands[3], 33.65)
    Fetchlands[4] = np.append(Fetchlands[4], 63.75)
    Fetchlands[5] = np.append(Fetchlands[5], 24.68)
    Fetchlands[6] = np.append(Fetchlands[6], 62.40)
    Fetchlands[7] = np.append(Fetchlands[7], 54.99)
    Fetchlands[8] = np.append(Fetchlands[8], 15.94)
    Fetchlands[9] = np.append(Fetchlands[9], 27.13)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,9,2))
    
    #append the prices of the fetchlands for the next day(9/8/12020)//19
    Fetchlands[0] = np.append(Fetchlands[0], 30.41)
    Fetchlands[1] = np.append(Fetchlands[1], 25.97)
    Fetchlands[2] = np.append(Fetchlands[2], 20.02)
    Fetchlands[3] = np.append(Fetchlands[3], 32.76)
    Fetchlands[4] = np.append(Fetchlands[4], 62.21)
    Fetchlands[5] = np.append(Fetchlands[5], 27.00)
    Fetchlands[6] = np.append(Fetchlands[6], 55.35)
    Fetchlands[7] = np.append(Fetchlands[7], 48.63)
    Fetchlands[8] = np.append(Fetchlands[8], 15.63)
    Fetchlands[9] = np.append(Fetchlands[9], 27.35)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,9,8))
    
    filepath = os.path.join('C:/Users/backup/Fetchland_Prices', 'Fetchland_prices.txt')
    if not os.path.exists('C:/Users/backup/Fetchland_Prices'):
        os.makedirs('C:/Users/backup/Fetchland_Prices')
    f = open(filepath, 'w')
    for i in range(0,11):
        for j in range(0,19):
            f.write(str(Fetchlands[i][j]))
            f.write(', ')
        f.write('\n')
    f.close()

#runs the function is called from the command line  
FetchpriceW()
    