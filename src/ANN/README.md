#Artificial Neural Network

Using ANNs is one of the ways I'll try to model the problem of determine the time to buy or sell a stock.

##Input
Here is the data I'll try to use as input:
	* The closing price of the last x days.
	* The opening price of the last x days.
	* The maximum price of the last x days.
	* The minimum price of the last x days.
	* Simple Moving Average (SMA) of the closing price of the last x days.
	* Exponential Moving Average (EMA) of the closing price of the last x days.
	* A ratio defined by EMA / SMA of the closing price of the last x days.
	* Bollinger Bands
	* MACD

Just to be clear, I'll not use every single one of them in one network, but combinations of them. The results with data like efficiency of each network will be posted on the doc folder.

To begin, I'll test the ANN's with the number of days x being 5, 7, 10 or 15 days.


##Output
The output will be one node, its value will be on the range of [-1, 1].

##Activation Function
The activation function will be given by:<br/><img src="http://i.imgur.com/0YKOq9G.png" align="center" border="0" alt="" />
