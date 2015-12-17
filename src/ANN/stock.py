#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stock:
  
  def __init__(self, pname, pperiod_size):
    self.name = pname
    self.period_size = pperiod_size
    self.data = []
    self.yearLimits = None
  
  
  def loadData(self, path):
    '''
      This method grab the file path of the stock and loads its data.
    '''
    
    if path[-1] != '/':
      path += '/'
    
    path += self.name+'_'+str(self.period_size)
    
    # Order: [Closing Price] [Opening Price] [SMA] [EMA] [SMA/EMA] [Standard Score] [Standard Deviation] [Upper Band] [Lower Band] [Date]
    inFile = open(path, 'r')
    for line in inFile.readlines():
      splitted_line = line.split(' ')
      neue_data = {}
      neue_data['closing'] = float(splitted_line[0])
      neue_data['opening'] = float(splitted_line[1])
      neue_data['sma'] = float(splitted_line[2])
      neue_data['ema'] = float(splitted_line[3])
      neue_data['emadivsma'] = float(splitted_line[4])
      neue_data['sscore'] = float(splitted_line[5])
      neue_data['sdeviation'] = float(splitted_line[6])
      neue_data['upperbbands'] = float(splitted_line[7])
      neue_data['lowerbbands'] = float(splitted_line[8])
      neue_data['date'] = splitted_line[9]
      self.data.append(neue_data)
    inFile.close()

    # Preprocessing the year limits
    self.yearLimits = {}
    for i in range(2010, 2016):
      self.yearLimits[i] = self.preprocessYearLimits(i)
    

  
  def getName(self):
    return self.name
  
  
  def getPeriodSize(self):
    return self.period_size
  
  
  def getData(self, index=-1):
    if index < 0:
      return self.data
    else:
      return self.data[index]
  
  
  def preprocessYearLimits(self, year):
    first, last = -1, -1
    for i in range(len(self.data)):
      if self.data[i]['date'][:4] == str(year):
        last = i
        if first == -1:
          first = last
    return [first, last]
  
  
  def getYearLimits(self, year):
    if self.yearLimits == None:
      raise Exception('Please, load the data first.')
    
    return self.yearLimits[int(year)]
  
  
