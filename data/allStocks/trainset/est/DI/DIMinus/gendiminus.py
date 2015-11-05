#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva
# 
# This script generates a bunch of files, where each file has the bollinger bands to a given setting.
# The stocks prices come from ../../daily_candles folder.
# 

import numpy
import talib
import sys
from os import listdir, makedirs
from os.path import isfile, join, exists

xDays = [5, 7, 10, 15, 21]
path = '../../../daily_candles'

def frange(b, e, s):
  while b < e:
    yield b
    b += s

def main():
  files = [ f for f in listdir(path) if isfile(join(path, f)) ]
  for f in files:
    close = maxi = mini = []
    paper_file = open(path+'/'+f, 'r')
    for line in paper_file.readlines():
      close.append(float(line.split(',')[0]))
      maxi.append(float(line.split(',')[2]))
      mini.append(float(line.split(',')[3]))

    close = numpy.array(close)
    maxi = numpy.array(maxi)
    mini = numpy.array(mini)
    paper_file.close()
    
    for x in xDays:
      value = talib.MINUS_DI(maxi, mini, close, x)
      outFile = open(f + "_"+ str(x) + '_diminus', 'w')
      for v in value:
        outFile.write(str(v))
        outFile.write("\n")
      outFile.close()


if __name__ == '__main__':
  main()
