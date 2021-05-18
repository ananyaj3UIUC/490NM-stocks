import mgarch
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from time import sleep
import pickle

'''
THIS FILE IS USED TO ANALYSE THE COVARIANCE MATRICES FROM EACH PAIR
EACH PAIR CAN BE ACCESSED IN DATA_DICT, WHICH LOADS IN A PICKLE FILE
TO ACCESS THE COVARIANCE MATRIX FOR A PARTICULAR STOCK PAIR, JUST WRITE
data_dict["stock1-stock2"]["cov"]
'''

data_dict = {}

with open('final_pair_dict.pickle', 'rb') as handle:
    data_dict = pickle.load(handle)

# Finding potential negatives covariance values
# (there are 118 matrices with negative covariances present out of the 600 total matrices)
count = 0
for i in data_dict.keys():
    if data_dict[i]['cov'][0][1] < 0 or data_dict[i]['cov'][1][0] < 0:
        print("NEGATIVE COVARIANCE FOUND IN " + i + "  ")
        count+=1

print("total negative covariance count is " + str(count) + " of 600 total pairs")