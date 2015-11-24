#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__= 'Thiago Silva'


from neuralnetwork import NeuralNetwork
import datahandler


interval_days_options=[5, 7, 10, 15, 21]


def readintervaldays():
  while True:
    try:
      interval_days = int(input('Interval days: '))
      if not interval_days in interval_days_options:
        raise NameError
      return interval_days
    except NameError:
      print 'Input just 5, 7, 10, 15 or 21'


def main():
  interval_days = readintervaldays()
  datahandler.load(interval_days)
  
  for stockName in datahandler.stock_list:
    nnetwork = NeuralNetwork()
    nnetwork.setSupervisedDataSetSize(9, 1)
    objStock = datahandler.getStock(stockName)
    neural_network_input = objStock.getData()
    
    print '##################################################################'
    print stockName
    print '##################################################################\n'
    
    total_tests=0
    total_hits=total_hits_highs=total_hits_lows=0
    total_highs=0
    total_lows=0
    # Sliding Window
    for i in range(len(neural_network_input)-3*interval_days):
      
      print str(i)+'th day'
      # Training
      for j in range(i+1, i+2*interval_days):
        input_data=[]
        output_data=[]
        for key, data in neural_network_input[j].iteritems():
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
      for j in range(i+2*interval_days, i+3*interval_days):
        input_data=[]
        for key, data in neural_network_input[j].iteritems():
          input_data.append(data)
        result = nnetwork.activate(input_data)
        hasRisen = neural_network_input[j-1]['closing'] < neural_network_input[j]['closing']
        output= 1 if hasRisen else 0
        
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
      print 'Last window:\n' + str(hits) + ' out of ' + str(interval_days)
      print str(hits_highs) + ' out of ' + str(highs) + ' highs.'
      print str(hits_lows) + ' out of ' + str(lows) + ' lows.'
      print 'Total:\n' + str(total_hits) + ' out of ' + str(total_tests)
      print str(total_hits_highs) + ' out of ' + str(total_highs) + ' highs.'
      print str(total_hits_lows) + ' out of ' + str(total_lows) + ' lows.' + '\n'


if __name__ == '__main__':
  main()
