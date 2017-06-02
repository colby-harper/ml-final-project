# Data set info
Using Quandl's free data set WIKI Prices - https://www.quandl.com/product/WIKIP/WIKI/PRICES-Quandl-End-Of-Day-Stocks-Info

Quandl Documentation - https://docs.quandl.com/docs/tables-3#section-filter-rows

# TODO
1. Finish loop by including ticker ID

2. create usable features
    1. (current price - prev price)/prev price
        2. (current volume - prev volume)/prev volume
        3. (current price - prev high)/prev high
        4. (current price - prev low)/prev low
        5. volatility? (prev high - prev low)/current

3. create output for prediction
	1. future price - current price
		1. change > 5% BUY 0
		2. change <5% & >-5% HOLD 1
		3. change < -5% SELL 2

4. run data through sklearn function

