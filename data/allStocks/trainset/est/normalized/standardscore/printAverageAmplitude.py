#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

import sys
import math


def main():
  filename = raw_input('Filename: ')
  inFile = open(filename, 'r')
  somass, somasd = 0.0, 0.0
  n = 0
  for line in inFile.readlines():
    n+=1
    splitted = line.split(' ')
    somass += math.fabs(float(splitted[0]))
    somasd += math.fabs(float(splitted[1]))
  print 'Standard Score Average: ' + str(somass/n)
  print 'Standard Deviation Average: ' + str(somasd/n)
  inFile.close()

if __name__ == '__main__':
  main()
