#!/usr/bin/env python
# -*- coding: utf-8 -*-

trainset_path = '../../data/allStocks/trainset/'
daily_candles_path = trainset_path+'daily_candles/'
averages_path = trainset_path+'est/averages/'
bollinger_bands_path = trainset_path+'est/Bollingerbands'
standard_score_path = trainset_path+'est/normalized/standardscore'


def getbbandsfilename(stockname, interval, bandwidth):
  '''
    This function returns the name of the file that keeps data about
    bollinger bands.
  '''
  return bollinger_bands_path+stockname+'_'+interval+'_'+bandwidth+'_closebbands'


def getaveragefilename(stockname, interval):
  '''
    This function returns the name of the file that keeps data about
    SMA and EMA, calculated with the closing prices.
  '''
  return averages_path+'_'+interval+'_closeSmaEma'


def getstandardscorefilename(stockname, interval):
  # TODO: Finish implementing this method after generating all the standard scores
  return standard_score_path+''


def getdailycandlesfilename(stockname):
  '''
    This function returns the name of the file that keeps
    the daily candles of a stock
  '''
  return averages_path+stockname


