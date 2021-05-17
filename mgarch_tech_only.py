import mgarch
import numpy as np
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from time import sleep

# serial key for alpha vantage
s_key = 'S2WB1VTMRBDU2XV3'

# alpha vantage time series data as a pandas object
time_series = TimeSeries(key=s_key, output_format = 'pandas')

'''
Measuring volativity difference for stock prices
Comparing industries
'''

# Tech companies: Amazon, Microsoft, Apple, Google, Facebook
tech_company_tags = ['AMZN', 'MSFT', 'AAPL', 'GOOG', 'FB']


# Energy companies
energy_company_tags = ['XOM', 'CVX', 'COP', 'TOT', 'BP']

# Financial company tags
finance_company_tags = ['JPM', 'BRK-A', 'BAC', 'C', 'WFC']

# Healthcare company tags
healthcare_company_tags = ['UNH', 'PFE', 'JNJ', 'MRK', 'ABT']

# Retail company tags
retail_company_tags = ['WMT', 'HD', 'COST', 'LOW', 'CVS']

# Dictionary mapping companies to a list of closing time stock prices
# Over the last 365 days (pandemic time)
tech_dict = {}
energy_dict = {}
finance_dict = {}
healthcare_dict = {}
retail_dict = {}


# I know this can be wrapped in a single loop but for now I'm keeping it separate
# Because its easier to modify each ones parameters individually if need be

# Filling dictionary for tech companies
for i in tech_company_tags:
    data_tech, info_tech = time_series.get_daily_adjusted(i, outputsize = 417)
    tech_dict[i] = data_tech['4. close'].to_numpy()
data_tech = np.concatenate([i[:,None] for i in tech_dict.values()], axis = 1)

# NEED to delay for at least one minute or i'll be accessing alpha vantage too quickly
x = data_tech
lt = np.log(x)
rt = lt[1:] - lt[:-1]
print(rt.shape)
vol = mgarch.mgarch('t')
model = vol.fit(rt)
cov_nextday = vol.predict(10)
print(cov_nextday)
print(cov_nextday['cov'].shape)