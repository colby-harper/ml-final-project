import pandas as pd 
import numpy as np 
import quandl
quandl.ApiConfig.api_key = "zCnMsnBTZogmUryumZCf"


def getData(link):
	data = pd.io.parsers.read_csv(
		filepath_or_buffer=link,
		skiprows = 1,
		header=None,
		sep=',')
	data.dropna(how='all', inplace=True)
	data.tail()
	return data 

def getStockPrices():
	#data = quandl.get("EIA/PET_RWTC_D", collapse="monthly")
	adj_close_data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, date = { 'gte': '2016-12-29', 'lte': '2016-12-31' }, paginate = True)
	#data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT'], date = { 'gte': '2016-01-01', 'lte': '2016-12-31' })
	ticker_data = quandl.get_table('WIKI/PRICES', qopts = {'columns': ['ticker']}, date = {'gte': '2016-12-30', 'lte': '2016-12-31'})
	# ticker_data = pd.io.parsers.read_csv(
	# 	filepath_or_buffer="https://www.quandl.com/api/v3/datatables/ETFG/FUND.csv?qopts.columns=ticker&api_key=zCnMsnBTZogmUryumZCf",
	# 	header=None,
	# 	sep='	')
	#print ticker_data
	for idex1, row1 in ticker_data.iterrows():
		for index, row in adj_close_data.iterrows():
			if row[0] == row1[0]:
				adj_close = row.adj_close
				ticker = row.ticker
				print ticker
				print adj_close
	#print ticker_data.ticker
	#print ticker_data

#def get_y_value():

#def set_x_value():

if __name__ == "__main__":

	#trianLink = 'https://api.usfundamentals.com/v1/indicators/xbrl?indicators=Assets,NetIncomeLoss&companies=320193&frequency=q&token=3E4utkNlSWRwP-3wmKru5w'
	#df = getData(trianLink)
	#print df
	getStockPrices()