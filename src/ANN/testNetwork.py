#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__= 'Thiago Silva'


from neuralnetwork import NeuralNetwork
import datahandler
import sys


interval_days_options=[5, 7, 10, 15, 21]


# This is the number of days the network will try to forecast after a set of training.
# This value can vary in [1, interval_days]
test_days=1


def readintervaldays():
  while True:
    try:
      interval_days = int(input('Interval days: '))
      if not interval_days in interval_days_options:
        raise NameError
      return interval_days
    except NameError:
      print 'Input just 5, 7, 10, 15 or 21'



def run_day(nnetwork, neural_network_input, day, interval_days, total_tests, total_hits, total_hits_highs, total_hits_lows, total_highs, total_lows):
  #sys.stdout.write(str(day)+'th day\n')
  # Training
  for j in range(day+1, day+2*interval_days):
    input_data=[]
    output_data=[]
    for key, data in neural_network_input[j].iteritems():
      if key == 'date':
        continue
      input_data.append(data)
    
    last_closing = neural_network_input[j-1]['closing']
    if last_closing > neural_network_input[j]['closing']:
      output_data.append(0)
    else:
      output_data.append(1)
    
    nnetwork.addTrainingSample(input_data, output_data)
  
  nnetwork.trainnetwork()

  # Testing
  hits=0
  hits_highs=highs=0
  hits_lows=lows=0
  standardDeviation=0
  network_result = []
  
  for j in range(day+2*interval_days, day+2*interval_days + test_days):
    input_data=[]
    for key, data in neural_network_input[j].iteritems():
      if key == 'date':
        continue
      input_data.append(data)
    result = nnetwork.activate(input_data)
    hasRisen = neural_network_input[j-1]['closing'] < neural_network_input[j]['closing']
    output = 1 if hasRisen else 0
    print str(result[0]) + ' ' + str(neural_network_input[j]['opening']) + ' ' + str(neural_network_input[j]['date'][:-1])
    network_result.append(result[0])
    
    if hasRisen:
      highs+=1
    else:
      lows+=1
    
    total_tests+=1
    if (result[0] > 0.5 and hasRisen) or (result[0] <= 0.5 and not hasRisen):
      hits+=1
    
    if result[0] > 0.5 and hasRisen:
      hits_highs+=1

    if result[0] <= 0.5 and not hasRisen:
      hits_lows+=1
  
  total_highs+=highs
  total_lows+=lows
  total_hits_highs+=hits_highs
  total_hits_lows+=hits_lows
  total_hits+=hits
  #print 'Last window:\n' + str(hits) + ' out of ' + str(test_days)
  #print str(hits_highs) + ' out of ' + str(highs) + ' highs.'
  #print str(hits_lows) + ' out of ' + str(lows) + ' lows.'
  #print 'Total:\n' + str(total_hits) + ' out of ' + str(total_tests)
  #print str(total_hits_highs) + ' out of ' + str(total_highs) + ' highs.'
  #print str(total_hits_lows) + ' out of ' + str(total_lows) + ' lows.' + '\n'
  return [total_tests, total_hits, total_hits_highs, total_hits_lows, total_highs, total_lows, network_result]




def run(stockName, interval_days, year):
  nnetwork = NeuralNetwork()
  nnetwork.setSupervisedDataSetSize(9, 1)
  objStock = datahandler.getStock(stockName)
  neural_network_input = objStock.getData()
  yearLimits = objStock.getYearLimits(year)
  yearLimits[0] = max(0, yearLimits[0]-2*interval_days)
  
  #print '##################################################################'
  #print stockName
  #print '##################################################################\n'
  
  total_tests=0
  total_hits=total_hits_highs=total_hits_lows=0
  total_highs=total_lows=0
  
  # Sliding Window
  #for i in range(len(neural_network_input)-3*interval_days):
  for i in range(yearLimits[0], yearLimits[1]-3*interval_days):
    ret = run_day(nnetwork, neural_network_input, i, interval_days, total_tests, total_hits, total_hits_highs, total_hits_lows, total_highs, total_lows)
    total_tests = ret[0]
    total_hits = ret[1]
    total_hits_highs = ret[2]
    total_hits_lows = ret[3]
    total_highs = ret[4]
    total_lows = ret[5]
    
    rel_highs=rel_lows=''
    
    if total_highs==0:
      rel_highs = '-1'
    else:
      rel_highs = str(float(total_hits_highs)/total_highs)
    
    if total_lows==0:
      rel_lows='-1'
    else:
      rel_lows = str(float(total_hits_lows)/total_lows)
    
    rel_all = str(float(total_hits)/total_tests)
    
    #print 'All: ' + rel_all + '  High: ' + rel_highs + '  Low: ' + rel_lows
  print 'Total:\n' + str(total_hits) + ' out of ' + str(total_tests)
  print str(total_hits_highs) + ' out of ' + str(total_highs) + ' highs.'
  print str(total_hits_lows) + ' out of ' + str(total_lows) + ' lows.' + '\n'


def main():
  interval_days = readintervaldays()
  datahandler.load(interval_days)
  
  stockName = raw_input('Stock: ')
  year = input('Year: ')
  print ''
  run(stockName, interval_days, year)


if __name__ == '__main__':
  main()
