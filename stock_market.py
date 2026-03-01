import os.path
from datetime import timedelta
import yfinance as yf
import pandas as pd


# ================================= 1. FETCH DATA =================================
#  define tickers
filename = "ticker_data.csv"
tickers = ["^GSPC", "GC=F", "SI=F"]


# ------------------- ADD DATA OR UPDATE DATA IF ALREADY EXIST -------------------
# if the File exists, get the last date, and update if there is missing days
if os.path.exists(filename):
	existing    	= pd.read_csv(filename,index_col=0,parse_dates=True)#parse_dates=True
	last_date   	= existing.index[-1].date() 
	start_date		= last_date + timedelta(days=1) 
	new_data    	= yf.download(tickers,start=start_date,interval="1d")

	# if there is new_data → append to CSV. If it’s empty → skip writing to the CSV.
	if not new_data.empty:
		# Keep only dates after the last saved date
		new_data = new_data[new_data.index > pd.Timestamp(last_date)]
		if not new_data.empty:
			new_data.columns = ['_'.join(col).strip() for col in new_data.columns.values]
			new_data.to_csv(filename, mode='a', header=False)
			print(f"Added {len(new_data)} new rows.")
		else:
			print("No new data after filtering.")
	else:
		print("No new data to add.")










# File does not exist → fetch all history and create a CSV file
else:
	data = yf.download(tickers, period="max", interval="1d") 
	data.columns = ['_'.join(col).strip() for col in data.columns.values]
	data.to_csv(filename)
	print(f"File created with {len(data)} rows.")





'''
#for debugging
	print(f"Last date in CSV: {last_date}")
	print(f"Start date for download: {start_date}")
	print(f"First date in new_data: {new_data.index[0].date() if not new_data.empty else 'No data'}")
	print(f"Last date in new_data: {new_data.index[-1].date() if not new_data.empty else 'No data'}")
'''



# print(df.head())






# if f exist:
# only add today data. or (if I didn't run the code for a week) it will add all the missing days(days/weeks/months)
# if f not exist:
# run the code
# tickers = ["^GSPC", "GC=F"]
# data = yf.download(tickers, period="max",interval="1d") #period="max"
# print(data['Close']) # Show the closing prices
# data.to_csv("ticker_data.csv",mode='a') # write to a csv file