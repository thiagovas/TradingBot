#Artificial Neural Network

Using ANNs is one of the ways I'll try to model the problem of determine the time to buy or sell a stock.

##Input
Here is the data I'll try to use as input:<br/>
	* The closing price of the last x days.<br/>
	* The opening price of the last x days.<br/>
	* The maximum price of the last x days.<br/>
	* The minimum price of the last x days.<br/>
	* Simple Moving Average (SMA) of the closing price of the last x days.<br/>
	* Exponential Moving Average (EMA) of the closing price of the last x days.<br/>
	* A ratio defined by EMA / SMA of the closing price of the last x days.<br/>
	* Bollinger Bands.<br/>
	* MACD.<br/>

Just to be clear, I'll not use every single one of them in one network, but combinations of them. The results with data like efficiency of each network will be posted on the doc folder.

To begin, I'll test the ANN's with the number of days x being 5, 7, 10 or 15 days.


##Output
The output will be one node, its value will be on the range of [-1, 1].

##Activation Function
The activation function will be given by:<br/><img src="http://i.imgur.com/0YKOq9G.png" align="center" border="0" alt="\biggl S(t) = \[\frac{2}{1+e^t}-1\]"  width="145" height="45" />
