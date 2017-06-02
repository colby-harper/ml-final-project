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
	#array for new features
	features = np.zeros((data_array.shape[0],5))

	j = 0
	for i in range(0,data_array.shape[0]):
		#Check if in a new ticker group (skip first element if so)
		if (data_array[i][2] != j):
			j += 1
			i += 1
		#Calculate price percent difference - 1st column
		prev_price = data_array[i-1][0]
		price_diff = data_array[i][0] - prev_price
		features[i][0] = (price_diff)/(prev_price)
		
		#Calculate volume percent difference - 2nd column
		prev_vol = data_array[i-1][1]
		if (prev_vol == 0):
			features[i][1] = 1000
		else:
			vol_diff = data_array[i][1] - prev_vol
			features[i][1] = (vol_diff)/(prev_vol)

		#Calculate percent change from high

	print (features)
