import pandas as pd 
import numpy as np 
import quandl
quandl.ApiConfig.api_key = "zCnMsnBTZogmUryumZCf"



def getStockPrices():
	feature_data = quandl.get_table('WIKI/PRICES', ticker = ['CRIS', 'VVUS', 'CHK'], qopts = { 'columns': ['ticker', 'adj_close', 'adj_volume'] }, date = { 'gte': '2016-11-25', 'lte': '2016-12-31' })
	ticker_data = quandl.get_table('WIKI/PRICES', ticker = ['CRIS', 'VVUS', 'CHK'], qopts = {'columns': ['ticker']}, date = {'gte': '2016-12-30', 'lte': '2016-12-31'})
	#print "test"
	data_array = np.array([0,0])
	ticker_id = np.array([0])
	i = 0
	for index1, row1 in ticker_data.iterrows():
		print row1.ticker
		for index, row in feature_data.iterrows():
			if row.ticker == row1.ticker:
					adj_close = row.adj_close
					adj_volume = row.adj_volume
					newRow = np.array([adj_close, adj_volume])
					#print newRow
					data_array = np.vstack((data_array, newRow))
					ticker_id = np.vstack((ticker_id, i))
		i += 1

	ticker_id = ticker_id.astype(np.float64)
	data_array = np.append(data_array, ticker_id, 1)
	print data_array[1:]
	#print ticker_id
	np.savetxt("foo.txt", data_array)
#def get_y_value():

#def set_x_value():

if __name__ == "__main__":

	getStockPrices()