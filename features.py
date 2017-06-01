import pandas as pd
import numpy as np
import math

def getData(link):
	data = pd.io.parsers.read_csv(
		filepath_or_buffer=link,
		skiprows = 1,
		header=None,
		sep=' ')
	data.dropna(how='all', inplace=True)
	data.tail()
	return data

if __name__ == "__main__":

	link = 'foo.txt'
	df = getData(link)
	print df