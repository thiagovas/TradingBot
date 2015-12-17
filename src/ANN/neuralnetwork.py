#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

import random
from math import sqrt, ceil
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet

class NeuralNetwork:
  
  def __init__(self):
    self.net = None
    self.trainer = None
    self.trainingSet = None
    self.input_size = 0
    self.output_size = 0
    self.hidden_nodes_size = 0
  
  
  def setSupervisedDataSetSize(self, pinput_size, poutput_size):
    '''
    '''
    self.input_size= pinput_size
    self.output_size = poutput_size
    self.hidden_nodes_size = int(ceil(sqrt(pinput_size+poutput_size)))
    self.trainingSet = SupervisedDataSet(pinput_size, poutput_size)
  
  
  def addTrainingSample(self, input_data, output_data):
    '''
    '''
    self.trainingSet.addSample(input_data, output_data)
  
  
  def trainnetwork(self):
    '''
      This method trains the network using the input and output
      previously setted.
    '''
    self.net = buildNetwork(self.input_size, self.hidden_nodes_size,
                            self.output_size, bias=True)
    trainer = BackpropTrainer(self.net, self.trainingSet, learningrate=0.001, momentum=0.99)
    trainer.trainEpochs(100)
    
    
  def activate(self, input_data):
    '''
      This function receives new inputs and run them on the
      previous trained neural network
    '''
    if self.net == None:
      print 'You have to train the network first'
    return self.net.activate(input_data)

