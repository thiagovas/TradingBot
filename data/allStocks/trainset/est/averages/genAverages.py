#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva
# 
# This script generates a bunch of files, where each file has the SMA and EMA for each stock
# on the ../../daily_candles folder.
# 

import numpy
import talib
import sys
from os import listdir, makedirs
from os.path import isfile, join, exists

xDays = [5, 7, 10, 15, 21]
path = '../../daily_candles'

def main():
  files = [ f for f in listdir(path) if isfile(join(path, f)) ]
  for f in files:
    close = []
    paper_file = open(path+'/'+f, 'r')
    for line in paper_file.readlines():
      close.append(float(line.split(',')[0]))
    close = numpy.array(close)
    for x in xDays:
      sma = talib.SMA(close, timeperiod=x) # Simple Moving Average
      ema = talib.EMA(close, timeperiod=x) # Exponential Moving Average
      outFile = open(f + "_"+ str(x)+'_closeSmaEma', 'w')
      for i in range(len(sma)):
        outFile.write(str(sma[i]))
        outFile.write(' ')
        outFile.write(str(ema[i]))
        outFile.write(' ')
        outFile.write(str(ema[i]/sma[i]))
        outFile.write('\n')
      outFile.close()
    paper_file.close()
  

if __name__ == '__main__':
  main()
