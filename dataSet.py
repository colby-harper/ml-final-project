import pandas as pd 
import numpy as np 
import quandl
quandl.ApiConfig.api_key = "zCnMsnBTZogmUryumZCf"



def getStockPrices():
	feature_data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'adj_close', 'adj_volume'] }, date = { 'gte': '2016-12-29', 'lte': '2016-12-31' }, paginate = True)
	ticker_data = quandl.get_table('WIKI/PRICES', qopts = {'columns': ['ticker']}, date = {'gte': '2016-12-30', 'lte': '2016-12-31'})
	
	for index1, row1 in ticker_data.iterrows():
		for index, row in feature_data.iterrows():
			if row.ticker == row1.ticker:
				adj_close = row.adj_close
				ticker = row.ticker
				print ticker
				print adj_close

#def get_y_value():

#def set_x_value():

if __name__ == "__main__":

	getStockPrices()