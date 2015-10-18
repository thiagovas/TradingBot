__author__ = 'Thiago Silva'

import random
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet


dataModel = [
    [(0, 0), (0,)],
    [(0, 1), (1,)],
    [(1, 0), (1,)],
    [(1, 1), (0,)],
]

ds = SupervisedDataSet(2, 1)
for input, target in dataModel:
    ds.addSample(input, target)

random.seed()
trainingSet = SupervisedDataSet(2, 1)
for ri in range(0, 1000):
    input, target = dataModel[random.getrandbits(2)]
    trainingSet.addSample(input, target)

net = buildNetwork(2, 2, 1, bias=True)
trainer = BackpropTrainer(net, ds, learningrate=0.001, momentum=0.99)
trainer.trainUntilConvergence(verbose=True,
                              trainingData=trainingSet,
                              validationData=ds,
                              maxEpochs=10)

print '0,0->', net.activate([0,0])
print '0,1->', net.activate([0,1])
print '1,0->', net.activate([1,0])
print '1,1->', net.activate([1,1])
