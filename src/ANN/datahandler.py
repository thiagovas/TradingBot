#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

from stock import Stock

stock_data = {}
stock_list = ['ABEV3', 'BOVA11', 'CIEL3', 'CMIG4', 'EMBR3', 'ITUB4']
input_path = '../../data/allStocks/trainset/neuralNetworkInput/'


def load(period):
  for name in stock_list:
    stock_data[name] = Stock(name, period)
  
  for key, item in stock_data.iteritems():
    item.loadData(input_path)
  

def getStock(name):
  if not name in stock_list:
    raise NameError('Wrong stock name')
  
  return stock_data[name]
