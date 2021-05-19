#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:32:43 2021

@author: SSC
"""

import pickle
import matplotlib.pyplot as plt
from heapq import nsmallest 
from heapq import nlargest 


data_dict = {}

with open('final_pair_dict.pickle', 'rb') as handle:
    data_dict = pickle.load(handle)

print(data_dict.keys())


def get_cov(dict):
    output = []
    for stock in dict.keys():
        output.append(dict[stock]['cov'][1,0])
        
    return output

covs = get_cov(data_dict)

smallest_covs = nsmallest(3, covs)
largest_covs = nlargest(3, covs)

print(smallest_covs)
print(largest_covs)
smallestcovs_set = set(smallest_covs)
largestcovs_set = set(largest_covs) 

for i, val in enumerate(covs):
    if val in smallest_covs:
        print(i)

for i, val in enumerate(covs):
    if val in largest_covs:
        print(i)

keys_list = list(data_dict)

key1 = keys_list[56]
key2 = keys_list[104]
key3 = keys_list[109]
key4 = keys_list[174]
key5 = keys_list[224]
key6 = keys_list[349]

smallest_keys = [key1, key2, key3]
largest_keys = [key4, key5, key6]

print(smallest_keys)
print(largest_keys)

plt.scatter(data_dict.keys(),covs,s=5)
plt.title('Scatterplot of Stocks')
plt.xlabel('Pairs of Stocks')
plt.ylabel('Covariances')
