#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

import math
import sys

path = '../../../daily_candles/'

def main():
  filename = raw_input()
  inFile = open(path+filename, 'r')
  for line in inFile.readlines():
    splitted = line.split(',')
    for i in range(5):
      splitted[i] = math.log(float(splitted[0]))
    
    sys.stdout.write(str(splitted[0]))
    for i in range(1, len(splitted)):
      sys.stdout.write(',')
      sys.stdout.write(str(splitted[i]))
  inFile.close()
  

if __name__ == '__main__':
  main()
