import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm, tree
from sklearn.linear_model import LinearRegression
import math
#np.set_printoptions(threshold=np.nan)

def categorize(percent_change):
	stock_category = None
	if percent_change >= .1:
		stock_category = 0
	elif percent_change <= -.1:
		stock_category = 1
	else:
		stock_category = 2
	return stock_category

def getData(link):
	data = pd.io.parsers.read_csv(
		filepath_or_buffer=link,
		header=None,
		sep=' ')
	data.dropna(how='all', inplace=True)
	data.tail()
	return data

def calculateRMSE(yExpected , yActual , size):
	mse = 0
	for i in range(size):
		diff = yActual[i] - yExpected[i]
		mse += math.pow(diff,2)
	rmse = math.sqrt(mse/size)
	return rmse

def analysis(df):
	#print df
	X = np.array(df[:,:-2])
	y = np.array(df[:,-1])
	X = preprocessing.scale(X)
	cat = np.matrix(df[:,-2])
	cat = np.swapaxes(cat,0,1)
	X = np.append(X, cat, 1)
	#print X

	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=.2)

	train_cat = np.array(X_train[:,-1])
	X_train =np.delete(X_train, -1, axis=1)
	test_cat = np.array(X_test[:,-1])
	X_test = np.delete(X_test, -1, axis=1)
	# print X_test
	# print test_cat

	clf = svm.SVR(kernel = "poly",degree = 3)
	clf.fit(X_train,y_train)
	predictions = clf.predict(X_test)
	count = 0
	for i in range(len(predictions)-1):
		percent_change = ((predictions[i+1] - y_test[i])/y_test[i])*100
		predicted_cat = categorize(percent_change)
		if predicted_cat != test_cat[i+1]:
			#print "prediction: {} Actual: {}".format(predicted_cat, test_cat[i+1])
			count+=1
	print count

	#score = clf.score(X_test,y_test)
	#print (score)

	print(y_test)
	print(predictions)
	#y_test = preprocessing.normalize(y_test)
	#predictions = preprocessing.normalize(predictions)
	#print (y_train)

	rmse = calculateRMSE(y_test,predictions,y_test.shape[0])
	#print(y_test)
	#print(predictions)
	#print(predictions)
	print(rmse)

	#print("X: {},{}".format(X.shape[0],X.shape[1]))
	#print("y: {}".format(y.shape[0]))#,y.shape[1]))

if __name__ == "__main__":

	link = 'foo.txt'
	df = getData(link)
	#print (df)
	data_array = np.array(df)
	#array for new features
	features = np.zeros((data_array.shape[0],7))

	j = 0
	buy_count= hold_count= sell_count = 0
	for i in range(0,(data_array.shape[0]-2)):
		#Check if in a new ticker group (skip first element if so)
		if (data_array[i+2][5] != j):
			j = data_array[i+2][5]
			i += 3
		#Calculate price percent difference - 1st column
		prev_price = data_array[i-1][0]
		curr_price = data_array[i][0]
		price_diff = curr_price - prev_price
		features[i][0] = curr_price#(price_diff)/(prev_price)
		
		#Calculate volume percent difference - 2nd column
		#prev_vol = data_array[i-1][1]
		#vol_diff = data_array[i][1] - prev_vol
		features[i][1] = data_array[i][1]# (vol_diff)/(prev_vol)

		
		#Calculate percent change from high - 3rd column
		prev_high = data_array[i][2]
		price_diff_high = curr_price - prev_high
		features[i][2] = (price_diff_high)/prev_high

		#Calculate percent change from low - 4th column
		prev_low = data_array[i][3]
		price_diff_low = curr_price - prev_low
		features[i][3] = (price_diff_low)/prev_low

		#Calculate volatility - 5th column
		vola_diff = prev_high - prev_low
		features[i][4] = (vola_diff)/curr_price

		#future price - 6th clumn
		features[i][6] = data_array[i+2][4]

		#Calculate the future percent change - 7th column
		future_price = data_array[i+2][4]
		trade_price = data_array[i+1][4]
		percent_change = ((future_price - trade_price)/trade_price)*100
		#features[i][6] = percent_change
		stock_category = categorize(percent_change)
	
		features[i][5] = stock_category
	#get rid of zeros
	features = np.delete(features, 0, axis=0)
	features = np.delete(features, -1, axis=0)
	features = np.delete(features, -1, axis=0)

	increment = 274
	analysis(features[:increment])
	# print "# of buys: {}".format(buy_count)
	# print "# of sells: {}".format(sell_count)
	# print "# of holds: {}".format(hold_count)
	#print (features)
