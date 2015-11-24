#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

# Prints per line...
# [Standard Score] [Standard Deviation]


import math
import sys

stocks = ['ABEV3', 'BOVA11', 'CIEL3', 'CMIG4', 'EMBR3', 'ITUB4']

def main():
  for name in stocks:
    for period in [5, 7, 10, 15, 21]:
      filename = name+'_'+str(period)+'_closeSmaEma'
      inFile = open('../../averages/'+filename, 'r')
      lines = inFile.readlines()
      outFile = open(name+'_'+str(period), 'w')
      for i in range(len(lines)):
        splitted = lines[i].split(' ')
        if splitted[-2] == 'nan':
          outFile.write('nan nan\n')
        else:
          media = float(splitted[1])
          soma = 0.0
          for j in range(i-period+1, i+1):
            soma += (float(lines[j].split(' ')[0])-media)**2
          soma /= 5.0
          soma=math.sqrt(soma)
          outFile.write(str((float(splitted[0])-media)/soma))
          outFile.write(' ' + str(soma))
          outFile.write('\n')
      outFile.close()
      inFile.close()

if __name__ == '__main__':
  main()
