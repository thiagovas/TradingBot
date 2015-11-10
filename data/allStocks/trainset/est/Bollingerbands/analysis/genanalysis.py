#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva
# 
# 
# 

import sys

path='../'

def main():
  files = [ f for f in listdir(path) if (isfile(join(path, f)) and f[-5:]=='bands') ]
  for f in files:
    data = f.split('_')
    stock, period, deviation = data[0], data[1], data[2]
    inFile = open(path+f)
    allLines = inFile.readlines()
    for i in range(1, len(allLines)):
      
    inFile.close()
      
    


if __name__ == '__main__':
  main()
