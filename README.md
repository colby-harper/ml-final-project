# Data set info
Using Quandl's free data set WIKI Prices - https://www.quandl.com/product/WIKIP/WIKI/PRICES-Quandl-End-Of-Day-Stocks-Info

Quandl Documentation - https://docs.quandl.com/docs/tables-3#section-filter-rows

# TODO
-Finish loop by including ticker ID

-create usable features
	i. (current price - prev price)/prev price
	ii. (current volume - prev volume)/prev volume
	iii. (current price - prev high)/prev high
	iv. (current price - prev low)/prev low
	v. volatility? (prev high - prev low)/current

-create output for prediction
	future price - current price
		i. change > 5% BUY 0
		ii. change <5% & >-5% HOLD 1
		iii. change < -5% SELL 2

-run data through sklearn function

