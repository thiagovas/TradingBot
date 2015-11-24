#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Basically, it gets everything together in a file
# Averages
# Bollinger Bands
# Standard Score
# Closing Prices
# 
# OUTPUT PATTERN:
# [Closing Price] [Opening Price] [SMA] [EMA] [SMA/EMA] [Standard Score] [Standard Deviation] [Upper Band - BBands] [Lower Band - BBands]
# 
# 

import sys
from os import listdir, makedirs
from os.path import isfile, join, exists


stocks = ['ABEV3', 'BOVA11', 'CIEL3', 'CMIG4', 'EMBR3', 'ITUB4']


def getAveragesFilename(name, period):
  return '../est/averages/'+name+'_'+str(period)+'_closeSmaEma'


def getBBandsFilename(name, period):
  return '../est/Bollingerbands/'+name+'_'+str(period)+'_2.0_closebbands'


def getStandardScoreFilename(name, period):
  return '../est/normalized/standardscore/'+name+'_'+str(period)


def main():
  for period in [5, 7, 10, 15, 21]:
    for name in stocks:
      inFile = open(getAveragesFilename(name, period), 'r')
      averages = inFile.readlines()
      inFile.close()

      inFile = open(getBBandsFilename(name, period), 'r')
      bbands = inFile.readlines()
      inFile.close()

      inFile = open(getStandardScoreFilename(name, period), 'r')
      standardScore = inFile.readlines()
      inFile.close()
      
      outFile = open(name+'_'+str(period), 'w')
      for i in range(period-1, len(averages)):
        average_line = averages[i].split(' ')
        bbands_line = bbands[i].split(' ')
        standardScore_line = standardScore[i].split(' ')
        
        outFile.write(average_line[0] + ' ') # Closing Price
        outFile.write(average_line[4][:-1] + ' ') # Opening Price
        outFile.write(average_line[1] + ' ') # SMA
        outFile.write(average_line[2] + ' ') # EMA
        outFile.write(average_line[3] + ' ') # EMA/SMA
        
        outFile.write(standardScore_line[0] + ' ') # Standard Score
        outFile.write(standardScore_line[1][:-1] + ' ') # Standard Deviation
        
        outFile.write(bbands_line[1] + ' ') # Upper Band
        outFile.write(bbands_line[3][:-1] + '\n') # Lower Band
      
      outFile.close()  


if __name__ == '__main__':
  main()

