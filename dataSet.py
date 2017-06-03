import pandas as pd 
import numpy as np 
import quandl
from datetime import date
quandl.ApiConfig.api_key = "zCnMsnBTZogmUryumZCf"



def getStockPrices():
	
	initDate = date(2015,11,25)
	endDate = date(2016,12,31)

	ticker_list = []
	all_stocks = quandl.get_table('WIKI/PRICES', qopts = {'columns': ['ticker', 'adj_open']}, date = {'gte': initDate.strftime('%Y-%m-%d'), 'lte': initDate.strftime('%Y-%m-%d')})
	for index, row in all_stocks.iterrows():	
		if row.adj_open <= 5:
			ticker_list.append(str(row.ticker))

	feature_data = quandl.get_table('WIKI/PRICES', ticker = ticker_list, qopts = { 'columns': ['ticker', 'adj_close', 'adj_volume', 'adj_high', 'adj_low', 'date'] }, date = { 'gte': initDate.strftime('%Y-%m-%d'), 'lte': endDate.strftime('%Y-%m-%d') }, paginate=True)

	data_array = np.array([0,0,0,0])
	ticker_id = np.array([0])
	name = ''
	j = 0
	remove = set()
	for index, row in feature_data.iterrows():	
		if row.ticker != name:
			name = row.ticker
			j += 1
		adj_volume = row.adj_volume
		#If the volume is zero, add the ticker id to the remove set
		if (adj_volume == 0):	
			remove.add(j)

		adj_close = row.adj_close
		adj_high = row.adj_high
		adj_low = row.adj_low
		newRow = np.array([adj_close, adj_volume, adj_high, adj_low])
		data_array = np.vstack((data_array, newRow))
		ticker_id = np.vstack((ticker_id, j))
			
	ticker_id = ticker_id.astype(np.float64)
	data_array = np.append(data_array, ticker_id, 1)
	#loop through the array.  If a row's ticker id is in the set, delete that row.
	i = 0
	while i < len(data_array):
		if int(data_array[i,-1]) in remove:
			data_array = np.delete(data_array, (i), axis=0)
		else:
			i+=1
	#print(data_array.shape[0])
	np.savetxt("foo.txt", data_array[1:])
	
if __name__ == "__main__":

	getStockPrices()
