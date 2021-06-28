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
    
    #append the prices of the fetchlands for the next day(9/13/12020)//20
    Fetchlands[0] = np.append(Fetchlands[0], 31.45)
    Fetchlands[1] = np.append(Fetchlands[1], 25.93)
    Fetchlands[2] = np.append(Fetchlands[2], 19.00)
    Fetchlands[3] = np.append(Fetchlands[3], 33.35)
    Fetchlands[4] = np.append(Fetchlands[4], 64.76)
    Fetchlands[5] = np.append(Fetchlands[5], 23.79)
    Fetchlands[6] = np.append(Fetchlands[6], 57.37)
    Fetchlands[7] = np.append(Fetchlands[7], 51.45)
    Fetchlands[8] = np.append(Fetchlands[8], 14.93)
    Fetchlands[9] = np.append(Fetchlands[9], 25.64)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,9,13))
    
    #append the prices of the fetchlands for the next day(9/20/12020)//21
    Fetchlands[0] = np.append(Fetchlands[0], 31.91)
    Fetchlands[1] = np.append(Fetchlands[1], 25.36)
    Fetchlands[2] = np.append(Fetchlands[2], 19.00)
    Fetchlands[3] = np.append(Fetchlands[3], 36.41)
    Fetchlands[4] = np.append(Fetchlands[4], 66.59)
    Fetchlands[5] = np.append(Fetchlands[5], 24.01)
    Fetchlands[6] = np.append(Fetchlands[6], 60.37)
    Fetchlands[7] = np.append(Fetchlands[7], 55.44)
    Fetchlands[8] = np.append(Fetchlands[8], 14.86)
    Fetchlands[9] = np.append(Fetchlands[9], 25.38)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,9,20))
    
    #append the prices of the fetchlands for the next day(9/27/12020)//22
    Fetchlands[0] = np.append(Fetchlands[0], 32.59)
    Fetchlands[1] = np.append(Fetchlands[1], 25.75)
    Fetchlands[2] = np.append(Fetchlands[2], 18.95)
    Fetchlands[3] = np.append(Fetchlands[3], 34.19)
    Fetchlands[4] = np.append(Fetchlands[4], 68.22)
    Fetchlands[5] = np.append(Fetchlands[5], 26.57)
    Fetchlands[6] = np.append(Fetchlands[6], 60.95)
    Fetchlands[7] = np.append(Fetchlands[7], 55.37)
    Fetchlands[8] = np.append(Fetchlands[8], 15.68)
    Fetchlands[9] = np.append(Fetchlands[9], 25.67)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,9,27))
    
    #append the prices of the fetchlands for the next day(10/4/12020)//23
    Fetchlands[0] = np.append(Fetchlands[0], 31.45)
    Fetchlands[1] = np.append(Fetchlands[1], 25.90)
    Fetchlands[2] = np.append(Fetchlands[2], 20.61)
    Fetchlands[3] = np.append(Fetchlands[3], 30.61)
    Fetchlands[4] = np.append(Fetchlands[4], 66.61)
    Fetchlands[5] = np.append(Fetchlands[5], 27.34)
    Fetchlands[6] = np.append(Fetchlands[6], 58.08)
    Fetchlands[7] = np.append(Fetchlands[7], 49.91)
    Fetchlands[8] = np.append(Fetchlands[8], 16.54)
    Fetchlands[9] = np.append(Fetchlands[9], 26.58)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,10,4))
    
    #append the prices of the fetchlands for the next day(10/11/12020)//24
    Fetchlands[0] = np.append(Fetchlands[0], 34.72)
    Fetchlands[1] = np.append(Fetchlands[1], 24.57)
    Fetchlands[2] = np.append(Fetchlands[2], 20.76)
    Fetchlands[3] = np.append(Fetchlands[3], 34.25)
    Fetchlands[4] = np.append(Fetchlands[4], 65.31)
    Fetchlands[5] = np.append(Fetchlands[5], 27.97)
    Fetchlands[6] = np.append(Fetchlands[6], 60.25)
    Fetchlands[7] = np.append(Fetchlands[7], 51.89)
    Fetchlands[8] = np.append(Fetchlands[8], 16.64)
    Fetchlands[9] = np.append(Fetchlands[9], 26.57)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,10,11))
    
    #append the prices of the fetchlands for the next day(10/18/12020)//25
    Fetchlands[0] = np.append(Fetchlands[0], 33.85)
    Fetchlands[1] = np.append(Fetchlands[1], 24.88)
    Fetchlands[2] = np.append(Fetchlands[2], 20.22)
    Fetchlands[3] = np.append(Fetchlands[3], 34.99)
    Fetchlands[4] = np.append(Fetchlands[4], 66.24)
    Fetchlands[5] = np.append(Fetchlands[5], 27.42)
    Fetchlands[6] = np.append(Fetchlands[6], 60.10)
    Fetchlands[7] = np.append(Fetchlands[7], 52.54)
    Fetchlands[8] = np.append(Fetchlands[8], 15.91)
    Fetchlands[9] = np.append(Fetchlands[9], 24.00)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,10,18))
    
    #append the prices of the fetchlands for the next day(11/1/12020)//26
    Fetchlands[0] = np.append(Fetchlands[0], 33.34)
    Fetchlands[1] = np.append(Fetchlands[1], 24.41)
    Fetchlands[2] = np.append(Fetchlands[2], 20.08)
    Fetchlands[3] = np.append(Fetchlands[3], 34.67)
    Fetchlands[4] = np.append(Fetchlands[4], 68.61)
    Fetchlands[5] = np.append(Fetchlands[5], 26.98)
    Fetchlands[6] = np.append(Fetchlands[6], 59.06)
    Fetchlands[7] = np.append(Fetchlands[7], 49.54)
    Fetchlands[8] = np.append(Fetchlands[8], 16.87)
    Fetchlands[9] = np.append(Fetchlands[9], 24.68)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,11,1))
    
    #append the prices of the fetchlands for the next day(11/8/12020)//27
    Fetchlands[0] = np.append(Fetchlands[0], 29.25)
    Fetchlands[1] = np.append(Fetchlands[1], 23.15)
    Fetchlands[2] = np.append(Fetchlands[2], 18.71)
    Fetchlands[3] = np.append(Fetchlands[3], 33.66)
    Fetchlands[4] = np.append(Fetchlands[4], 67.65)
    Fetchlands[5] = np.append(Fetchlands[5], 25.66)
    Fetchlands[6] = np.append(Fetchlands[6], 55.11)
    Fetchlands[7] = np.append(Fetchlands[7], 49.10)
    Fetchlands[8] = np.append(Fetchlands[8], 16.61)
    Fetchlands[9] = np.append(Fetchlands[9], 23.47)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,11,8))
    
    #append the prices of the fetchlands for the next day(11/15/12020)//28
    Fetchlands[0] = np.append(Fetchlands[0], 29.65)
    Fetchlands[1] = np.append(Fetchlands[1], 23.28)
    Fetchlands[2] = np.append(Fetchlands[2], 18.51)
    Fetchlands[3] = np.append(Fetchlands[3], 32.64)
    Fetchlands[4] = np.append(Fetchlands[4], 66.07)
    Fetchlands[5] = np.append(Fetchlands[5], 25.71)
    Fetchlands[6] = np.append(Fetchlands[6], 55.79)
    Fetchlands[7] = np.append(Fetchlands[7], 47.98)
    Fetchlands[8] = np.append(Fetchlands[8], 15.35)
    Fetchlands[9] = np.append(Fetchlands[9], 24.17)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,11,15))
    
    #append the prices of the fetchlands for the next day(11/22/12020)//29
    Fetchlands[0] = np.append(Fetchlands[0], 29.75)
    Fetchlands[1] = np.append(Fetchlands[1], 23.13)
    Fetchlands[2] = np.append(Fetchlands[2], 18.31)
    Fetchlands[3] = np.append(Fetchlands[3], 30.99)
    Fetchlands[4] = np.append(Fetchlands[4], 64.15)
    Fetchlands[5] = np.append(Fetchlands[5], 25.68)
    Fetchlands[6] = np.append(Fetchlands[6], 56.92)
    Fetchlands[7] = np.append(Fetchlands[7], 46.33)
    Fetchlands[8] = np.append(Fetchlands[8], 13.68)
    Fetchlands[9] = np.append(Fetchlands[9], 23.09)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,11,22))
    
    #append the prices of the fetchlands for the next day(11/29/12020)//30
    Fetchlands[0] = np.append(Fetchlands[0], 28.56)
    Fetchlands[1] = np.append(Fetchlands[1], 21.92)
    Fetchlands[2] = np.append(Fetchlands[2], 17.71)
    Fetchlands[3] = np.append(Fetchlands[3], 31.76)
    Fetchlands[4] = np.append(Fetchlands[4], 64.71)
    Fetchlands[5] = np.append(Fetchlands[5], 23.72)
    Fetchlands[6] = np.append(Fetchlands[6], 53.82)
    Fetchlands[7] = np.append(Fetchlands[7], 45.64)
    Fetchlands[8] = np.append(Fetchlands[8], 14.06)
    Fetchlands[9] = np.append(Fetchlands[9], 20.19)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,11,29))
    
    #append the prices of the fetchlands for the next day(12/20/12020)//31
    Fetchlands[0] = np.append(Fetchlands[0], 30.86)
    Fetchlands[1] = np.append(Fetchlands[1], 21.77)
    Fetchlands[2] = np.append(Fetchlands[2], 18.10)
    Fetchlands[3] = np.append(Fetchlands[3], 31.87)
    Fetchlands[4] = np.append(Fetchlands[4], 54.74)
    Fetchlands[5] = np.append(Fetchlands[5], 22.86)
    Fetchlands[6] = np.append(Fetchlands[6], 50.21)
    Fetchlands[7] = np.append(Fetchlands[7], 42.64)
    Fetchlands[8] = np.append(Fetchlands[8], 14.19)
    Fetchlands[9] = np.append(Fetchlands[9], 21.88)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,12,20))
    
    #append the prices of the fetchlands for the next day(12/27/12020)//32
    Fetchlands[0] = np.append(Fetchlands[0], 30.23)
    Fetchlands[1] = np.append(Fetchlands[1], 22.22)
    Fetchlands[2] = np.append(Fetchlands[2], 17.90)
    Fetchlands[3] = np.append(Fetchlands[3], 32.00)
    Fetchlands[4] = np.append(Fetchlands[4], 54.21)
    Fetchlands[5] = np.append(Fetchlands[5], 22.79)
    Fetchlands[6] = np.append(Fetchlands[6], 50.25)
    Fetchlands[7] = np.append(Fetchlands[7], 40.35)
    Fetchlands[8] = np.append(Fetchlands[8], 14.71)
    Fetchlands[9] = np.append(Fetchlands[9], 22.18)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2020,12,27))
    
    #append the prices of the fetchlands for the next day(1/3/12021)//33
    Fetchlands[0] = np.append(Fetchlands[0], 30.05)
    Fetchlands[1] = np.append(Fetchlands[1], 22.51)
    Fetchlands[2] = np.append(Fetchlands[2], 18.60)
    Fetchlands[3] = np.append(Fetchlands[3], 32.22)
    Fetchlands[4] = np.append(Fetchlands[4], 57.29)
    Fetchlands[5] = np.append(Fetchlands[5], 23.96)
    Fetchlands[6] = np.append(Fetchlands[6], 51.80)
    Fetchlands[7] = np.append(Fetchlands[7], 41.58)
    Fetchlands[8] = np.append(Fetchlands[8], 14.74)
    Fetchlands[9] = np.append(Fetchlands[9], 22.64)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,1,3))
    
    #append the prices of the fetchlands for the next day(1/10/12021)//34
    Fetchlands[0] = np.append(Fetchlands[0], 30.55)
    Fetchlands[1] = np.append(Fetchlands[1], 22.92)
    Fetchlands[2] = np.append(Fetchlands[2], 19.72)
    Fetchlands[3] = np.append(Fetchlands[3], 32.83)
    Fetchlands[4] = np.append(Fetchlands[4], 59.82)
    Fetchlands[5] = np.append(Fetchlands[5], 24.31)
    Fetchlands[6] = np.append(Fetchlands[6], 53.80)
    Fetchlands[7] = np.append(Fetchlands[7], 44.73)
    Fetchlands[8] = np.append(Fetchlands[8], 15.23)
    Fetchlands[9] = np.append(Fetchlands[9], 23.05)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,1,10))
    
    #append the prices of the fetchlands for the next day(1/17/12021)//35
    Fetchlands[0] = np.append(Fetchlands[0], 31.02)
    Fetchlands[1] = np.append(Fetchlands[1], 23.40)
    Fetchlands[2] = np.append(Fetchlands[2], 19.53)
    Fetchlands[3] = np.append(Fetchlands[3], 33.36)
    Fetchlands[4] = np.append(Fetchlands[4], 61.40)
    Fetchlands[5] = np.append(Fetchlands[5], 24.09)
    Fetchlands[6] = np.append(Fetchlands[6], 55.00)
    Fetchlands[7] = np.append(Fetchlands[7], 46.12)
    Fetchlands[8] = np.append(Fetchlands[8], 16.21)
    Fetchlands[9] = np.append(Fetchlands[9], 22.66)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,1,17))
    
    #append the prices of the fetchlands for the next day(2/7/12021)//36
    Fetchlands[0] = np.append(Fetchlands[0], 32.26)
    Fetchlands[1] = np.append(Fetchlands[1], 25.25)
    Fetchlands[2] = np.append(Fetchlands[2], 21.19)
    Fetchlands[3] = np.append(Fetchlands[3], 34.65)
    Fetchlands[4] = np.append(Fetchlands[4], 63.55)
    Fetchlands[5] = np.append(Fetchlands[5], 23.75)
    Fetchlands[6] = np.append(Fetchlands[6], 54.53)
    Fetchlands[7] = np.append(Fetchlands[7], 45.38)
    Fetchlands[8] = np.append(Fetchlands[8], 17.20)
    Fetchlands[9] = np.append(Fetchlands[9], 25.78)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,2,7))
    
    #append the prices of the fetchlands for the next day(2/14/12021)//37
    Fetchlands[0] = np.append(Fetchlands[0], 32.40)
    Fetchlands[1] = np.append(Fetchlands[1], 24.47)
    Fetchlands[2] = np.append(Fetchlands[2], 21.31)
    Fetchlands[3] = np.append(Fetchlands[3], 34.88)
    Fetchlands[4] = np.append(Fetchlands[4], 63.99)
    Fetchlands[5] = np.append(Fetchlands[5], 22.94)
    Fetchlands[6] = np.append(Fetchlands[6], 52.63)
    Fetchlands[7] = np.append(Fetchlands[7], 45.89)
    Fetchlands[8] = np.append(Fetchlands[8], 16.41)
    Fetchlands[9] = np.append(Fetchlands[9], 24.73)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,2,14))
    
    #append the prices of the fetchlands for the next day(2/28/12021)//38
    Fetchlands[0] = np.append(Fetchlands[0], 31.63)
    Fetchlands[1] = np.append(Fetchlands[1], 24.38)
    Fetchlands[2] = np.append(Fetchlands[2], 18.43)
    Fetchlands[3] = np.append(Fetchlands[3], 35.49)
    Fetchlands[4] = np.append(Fetchlands[4], 63.87)
    Fetchlands[5] = np.append(Fetchlands[5], 28.26)
    Fetchlands[6] = np.append(Fetchlands[6], 54.58)
    Fetchlands[7] = np.append(Fetchlands[7], 46.05)
    Fetchlands[8] = np.append(Fetchlands[8], 15.50)
    Fetchlands[9] = np.append(Fetchlands[9], 24.53)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,2,28))
    
    #append the prices of the fetchlands for the next day(3/28/12021)//39
    Fetchlands[0] = np.append(Fetchlands[0], 37.54)
    Fetchlands[1] = np.append(Fetchlands[1], 36.76)
    Fetchlands[2] = np.append(Fetchlands[2], 25.57)
    Fetchlands[3] = np.append(Fetchlands[3], 40.48)
    Fetchlands[4] = np.append(Fetchlands[4], 68.15)
    Fetchlands[5] = np.append(Fetchlands[5], 37.59)
    Fetchlands[6] = np.append(Fetchlands[6], 59.73)
    Fetchlands[7] = np.append(Fetchlands[7], 54.11)
    Fetchlands[8] = np.append(Fetchlands[8], 22.51)
    Fetchlands[9] = np.append(Fetchlands[9], 35.95)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,3,28))
    
    #append the prices of the fetchlands for the next day(4/4/12021)//40
    Fetchlands[0] = np.append(Fetchlands[0], 39.36)
    Fetchlands[1] = np.append(Fetchlands[1], 37.45)
    Fetchlands[2] = np.append(Fetchlands[2], 25.21)
    Fetchlands[3] = np.append(Fetchlands[3], 41.37)
    Fetchlands[4] = np.append(Fetchlands[4], 69.83)
    Fetchlands[5] = np.append(Fetchlands[5], 42.15)
    Fetchlands[6] = np.append(Fetchlands[6], 67.21)
    Fetchlands[7] = np.append(Fetchlands[7], 58.84)
    Fetchlands[8] = np.append(Fetchlands[8], 21.47)
    Fetchlands[9] = np.append(Fetchlands[9], 33.93)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,4,4))
    
    #append the prices of the fetchlands for the next day(4/11/12021)//41
    Fetchlands[0] = np.append(Fetchlands[0], 40.60)
    Fetchlands[1] = np.append(Fetchlands[1], 34.97)
    Fetchlands[2] = np.append(Fetchlands[2], 27.24)
    Fetchlands[3] = np.append(Fetchlands[3], 41.30)
    Fetchlands[4] = np.append(Fetchlands[4], 72.47)
    Fetchlands[5] = np.append(Fetchlands[5], 43.87)
    Fetchlands[6] = np.append(Fetchlands[6], 68.89)
    Fetchlands[7] = np.append(Fetchlands[7], 62.32)
    Fetchlands[8] = np.append(Fetchlands[8], 22.68)
    Fetchlands[9] = np.append(Fetchlands[9], 35.50)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,4,11))
    
    #append the prices of the fetchlands for the next day(4/18/12021)//42
    Fetchlands[0] = np.append(Fetchlands[0], 40.28)
    Fetchlands[1] = np.append(Fetchlands[1], 33.74)
    Fetchlands[2] = np.append(Fetchlands[2], 29.35)
    Fetchlands[3] = np.append(Fetchlands[3], 44.68)
    Fetchlands[4] = np.append(Fetchlands[4], 71.82)
    Fetchlands[5] = np.append(Fetchlands[5], 40.93)
    Fetchlands[6] = np.append(Fetchlands[6], 70.43)
    Fetchlands[7] = np.append(Fetchlands[7], 61.56)
    Fetchlands[8] = np.append(Fetchlands[8], 24.17)
    Fetchlands[9] = np.append(Fetchlands[9], 37.70)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,4,18))
    
    #append the prices of the fetchlands for the next day(4/25/12021)//43
    Fetchlands[0] = np.append(Fetchlands[0], 40.60)
    Fetchlands[1] = np.append(Fetchlands[1], 32.19)
    Fetchlands[2] = np.append(Fetchlands[2], 30.36)
    Fetchlands[3] = np.append(Fetchlands[3], 44.63)
    Fetchlands[4] = np.append(Fetchlands[4], 73.01)
    Fetchlands[5] = np.append(Fetchlands[5], 39.73)
    Fetchlands[6] = np.append(Fetchlands[6], 69.67)
    Fetchlands[7] = np.append(Fetchlands[7], 61.83)
    Fetchlands[8] = np.append(Fetchlands[8], 22.83)
    Fetchlands[9] = np.append(Fetchlands[9], 34.77)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,4,25))
    
    #append the prices of the fetchlands for the next day(5/9/12021)//44
    Fetchlands[0] = np.append(Fetchlands[0], 42.09)
    Fetchlands[1] = np.append(Fetchlands[1], 34.07)
    Fetchlands[2] = np.append(Fetchlands[2], 26.38)
    Fetchlands[3] = np.append(Fetchlands[3], 45.31)
    Fetchlands[4] = np.append(Fetchlands[4], 71.14)
    Fetchlands[5] = np.append(Fetchlands[5], 37.23)
    Fetchlands[6] = np.append(Fetchlands[6], 71.50)
    Fetchlands[7] = np.append(Fetchlands[7], 66.51)
    Fetchlands[8] = np.append(Fetchlands[8], 22.07)
    Fetchlands[9] = np.append(Fetchlands[9], 32.88)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,5,9))
    
    #append the prices of the fetchlands for the next day(5/16/12021)//45
    Fetchlands[0] = np.append(Fetchlands[0], 42.19)
    Fetchlands[1] = np.append(Fetchlands[1], 35.84)
    Fetchlands[2] = np.append(Fetchlands[2], 27.04)
    Fetchlands[3] = np.append(Fetchlands[3], 43.98)
    Fetchlands[4] = np.append(Fetchlands[4], 70.83)
    Fetchlands[5] = np.append(Fetchlands[5], 39.67)
    Fetchlands[6] = np.append(Fetchlands[6], 67.35)
    Fetchlands[7] = np.append(Fetchlands[7], 64.67)
    Fetchlands[8] = np.append(Fetchlands[8], 20.13)
    Fetchlands[9] = np.append(Fetchlands[9], 35.68)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,5,16))
    
    #append the prices of the fetchlands for the next day(5/23/12021)//46
    Fetchlands[0] = np.append(Fetchlands[0], 40.00)
    Fetchlands[1] = np.append(Fetchlands[1], 33.30)
    Fetchlands[2] = np.append(Fetchlands[2], 28.20)
    Fetchlands[3] = np.append(Fetchlands[3], 43.31)
    Fetchlands[4] = np.append(Fetchlands[4], 67.40)
    Fetchlands[5] = np.append(Fetchlands[5], 36.13)
    Fetchlands[6] = np.append(Fetchlands[6], 66.57)
    Fetchlands[7] = np.append(Fetchlands[7], 63.79)
    Fetchlands[8] = np.append(Fetchlands[8], 20.30)
    Fetchlands[9] = np.append(Fetchlands[9], 36.30)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,5,23))
    
    #append the prices of the fetchlands for the next day(6/13/12021)//47
    Fetchlands[0] = np.append(Fetchlands[0], 23.21)
    Fetchlands[1] = np.append(Fetchlands[1], 36.37)
    Fetchlands[2] = np.append(Fetchlands[2], 26.49)
    Fetchlands[3] = np.append(Fetchlands[3], 23.40)
    Fetchlands[4] = np.append(Fetchlands[4], 39.23)
    Fetchlands[5] = np.append(Fetchlands[5], 40.69)
    Fetchlands[6] = np.append(Fetchlands[6], 37.50)
    Fetchlands[7] = np.append(Fetchlands[7], 36.83)
    Fetchlands[8] = np.append(Fetchlands[8], 23.65)
    Fetchlands[9] = np.append(Fetchlands[9], 38.48)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,6,13))
    
    #append the prices of the fetchlands for the next day(6/20/12021)//48
    Fetchlands[0] = np.append(Fetchlands[0], 23.66)
    Fetchlands[1] = np.append(Fetchlands[1], 36.95)
    Fetchlands[2] = np.append(Fetchlands[2], 29.68)
    Fetchlands[3] = np.append(Fetchlands[3], 22.62)
    Fetchlands[4] = np.append(Fetchlands[4], 37.28)
    Fetchlands[5] = np.append(Fetchlands[5], 40.01)
    Fetchlands[6] = np.append(Fetchlands[6], 41.90)
    Fetchlands[7] = np.append(Fetchlands[7], 35.80)
    Fetchlands[8] = np.append(Fetchlands[8], 23.49)
    Fetchlands[9] = np.append(Fetchlands[9], 39.92)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,6,20))
    
    #append the prices of the fetchlands for the next day(6/27/12021)//49
    Fetchlands[0] = np.append(Fetchlands[0], 25.10)
    Fetchlands[1] = np.append(Fetchlands[1], 45.87)
    Fetchlands[2] = np.append(Fetchlands[2], 38.71)
    Fetchlands[3] = np.append(Fetchlands[3], 24.51)
    Fetchlands[4] = np.append(Fetchlands[4], 41.95)
    Fetchlands[5] = np.append(Fetchlands[5], 44.40)
    Fetchlands[6] = np.append(Fetchlands[6], 41.53)
    Fetchlands[7] = np.append(Fetchlands[7], 39.56)
    Fetchlands[8] = np.append(Fetchlands[8], 31.61)
    Fetchlands[9] = np.append(Fetchlands[9], 48.51)
    Fetchlands[10] = np.append(Fetchlands[10], datetime.date(2021,6,27))
    
    filepath = os.path.join('C:/Users/backup/Fetchland_Prices', 'Fetchland_prices.txt')
    if not os.path.exists('C:/Users/backup/Fetchland_Prices'):
        os.makedirs('C:/Users/backup/Fetchland_Prices')
    f = open(filepath, 'w')
    for i in range(0,11):
        for j in range(0,49):
            f.write(str(Fetchlands[i][j]))
            f.write(', ')
        f.write('\n')
    f.close()

#runs the function is called from the command line  
FetchpriceW()
    