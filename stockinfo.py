import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData

# serial key for alpha vantage
s_key = 'S2WB1VTMRBDU2XV3'

# alpha vantage time series data and fundamental data as a pandas object
time_series = TimeSeries(key=s_key, output_format = 'pandas')
fund_data = FundamentalData(key = s_key, output_format = 'pandas')

# EXAMPLE: printing ALL data points for Apple (AAPL)
aapl_time_series = time_series.get_daily_adjusted('AAPL', outputsize='full')
#print(aapl_time_series)

# EXAMPLE: printing Apple (AAPL) annual income statements
aapl_income_statements = fund_data.get_income_statement_annual('AAPL')
#print(aapl_income_statements)

# sec data imported from the CSV file
sec_data = pd.read_csv('cik_ticker.csv', sep = '|')

# filtered to only top 100 (alphabetical) NYSE companies
t100_nyse = sec_data[sec_data["Exchange"] == "NYSE"].head(100)

# SIC codes are actually already present in the CSV, we can filter by SIC code
# For example, 7389 is for business services
t100_nyse_business_services_sector = t100_nyse[t100_nyse["SIC"] == 7389]
#print(t100_nyse_business_services_sector)

# Binding SIC values to NAICS values where there exists a valid conversion
# If there is no valid conversion, the NAICS value is placed as 000000

conversion_table = pd.read_csv('converter.csv', sep = ",", encoding = 'cp1252')
t100_nyse['NAICS'] = pd.Series(['0']*len(sec_data['SIC']))

# A lot of conversion errors and mismatched data types need to be handled
# But for the most part it works fine
for index, row in t100_nyse.iterrows():
    if row['SIC'] == None or row['SIC'] == '':
       t100_nyse.loc[index, 'NAICS'] = '000000'
       continue
    try:
        try:
            code = str(int(row['SIC']))
            converted = str(conversion_table[conversion_table['SIC'] == code]['NAICS'].values[0])
            t100_nyse.loc[index, 'NAICS'] = converted
        except IndexError:
            t100_nyse.loc[index, 'NAICS'] = '000000'
            continue

    except ValueError:
        t100_nyse.loc[index, 'NAICS'] = '000000'
        continue
    

# Printing the UPDATED t100_nyse data frame with the new NAICS field
#for index, row in t100_nyse.iterrows(): print(row)

bad_naics = t100_nyse[t100_nyse['NAICS'] == '000000']

for index, row in bad_naics.iterrows(): print(row)