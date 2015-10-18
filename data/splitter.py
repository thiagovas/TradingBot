#/usr/env/python
# -*- coding: utf-8 -*-
#
# This piece of code, basically splits that big file with all stocks into several files,
# each file with data about just one stock.
#
# By Thiago Silva

import sys

DIR="./allStocks/15min_candles/"

allStocks = set()
sys.stdin.readline() # Ignoring the header...
stocks={};
for line in sys.stdin:
    stockName = line.split(',')[0]
    value = line[line.find(',')+1:]
    allStocks.add(stockName)
    try:
        stocks[line.split(',')[0]].append(value)
    except KeyError:
        stocks[line.split(',')[0]] = [value]

for s, l in stocks.iteritems():
    f = open(DIR+s, 'w')
    for value in l:
       f.write(value) 
    f.close()

stockfile = open('stocks_list', 'w')
for value in allStocks:
    stockfile.write(value+"\n");
stockfile.close();
