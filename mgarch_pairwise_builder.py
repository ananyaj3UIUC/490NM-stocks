import mgarch
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from time import sleep
import pickle

stock_dict = {}

with open('data.pickle', 'rb') as handle:
    stock_dict = pickle.load(handle)

x = list(stock_dict.keys())


cov_matrix_dict = {}


counter = 0
for i in range(0, len(x) - 1):
    for j in range(1, len(x)):
        data = np.concatenate((stock_dict[x[i]][:,None], stock_dict[x[j]][:,None]), axis = 1)
        lt = np.log(data)
        rt = lt[1:] - lt[:-1]
        vol = mgarch.mgarch('t')
        vol.fit(rt)
        cov_nextday = vol.predict(10)
        cov_matrix_dict[x[i] + '-'  + x[j]] = (cov_nextday)
        print(x[i] + '-'  + x[j])
        counter += 1
        print(str((counter / 600)*100) + '%')


with open('final_pair_dict.pickle', 'wb') as handle:
    pickle.dump(cov_matrix_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

        




    


        


