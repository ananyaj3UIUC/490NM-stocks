import mgarch
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from time import sleep
import pickle

# serial key for alpha vantage
s_key = 'S2WB1VTMRBDU2XV3'

# alpha vantage time series data as a pandas object
time_series = TimeSeries(key=s_key, output_format = 'pandas')

'''
Measuring volativity difference for stock prices
Comparing industries
'''

final_dict = {}

# Tech companies: Amazon, Microsoft, Apple, Google, Facebook
tech_company_tags = ['AMZN', 'MSFT', 'AAPL', 'GOOG', 'FB']
for i in tech_company_tags: final_dict[i] = None

# Energy companies
energy_company_tags = ['XOM', 'CVX', 'COP', 'TOT', 'BP']
for i in energy_company_tags: final_dict[i] = None

# Financial company tags
finance_company_tags = ['JPM', 'BRK-A', 'BAC', 'C', 'WFC']
for i in finance_company_tags: final_dict[i] = None

# Healthcare company tags
healthcare_company_tags = ['UNH', 'PFE', 'JNJ', 'MRK', 'ABT']
for i in healthcare_company_tags: final_dict[i] = None

# Retail company tags
retail_company_tags = ['WMT', 'HD', 'COST', 'LOW', 'CVS']
for i in retail_company_tags: final_dict[i] = None

sleep_counter = 1
for i in final_dict.keys():
    data, info = time_series.get_daily_adjusted(i, outputsize = 417)
    final_dict[i] = data['4. close'].to_numpy()
    sleep_counter+=1
    if sleep_counter % 5 == 0: sleep(70)

with open('data.pickle', 'wb') as handle:
    pickle.dump(final_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

