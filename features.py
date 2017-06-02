import pandas as pd
import numpy as np
import math

def getData(link):
	data = pd.io.parsers.read_csv(
		filepath_or_buffer=link,
		header=None,
		sep=' ')
	data.dropna(how='all', inplace=True)
	data.tail()
	return data

if __name__ == "__main__":

	link = 'foo.txt'
	df = getData(link)
	#print (df)
	data_array = np.array(df)
	#take the tickers off for now to add features, will put ticker on at very end
	ticker_array = data_array[:,2]
	ticker_array = np.reshape(ticker_array,(-1,1))
	#print(ticker_array)
	data_array = np.delete(data_array,2,1)
	#print (ticker_array)
	new_features = np.zeros((data_array.shape[0],5))
	data_array = np.append(data_array,np.append(new_features,ticker_array,1),1)
	#print(data_array)
	j = 0
	for i in range(0,data_array.shape[0]):
		#Check if in a new ticker group (skip first element if so)
		if (data_array[i][7] != j):
			j += 1
			i += 1
		#Calculate price percent difference - 3rd column
		prev_price = data_array[i-1][0]
		price_diff = data_array[i][0] - prev_price
		data_array[i][2] = (price_diff)/(prev_price)
		
		#Calculate volume percent difference - 4th column
		prev_vol = data_array[i-1][1]
		if (prev_vol == 0):
			data_array[i][3] = 1000
		else:
			vol_diff = data_array[i][1] - prev_vol
			data_array[i][3] = (vol_diff)/(prev_vol)

		#Calculate percent change from high

	data_array = np.delete(data_array,7,1)
	print (data_array)
