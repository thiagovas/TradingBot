#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

# Prints per line...
# [Standard Score] [Standard Deviation]


import math
import sys

def main():
  filename = raw_input()
  inFile = open(filename, 'r')
  lines = inFile.readlines()
  for i in range(len(lines)):
    splitted = lines[i].split(' ')
    if splitted[-2] == 'nan':
      continue
    else:
      media = float(splitted[1])
      soma = 0.0
      for j in range(i-4, i+1):
        soma += (float(lines[j].split(' ')[0])-media)**2
      soma /= 5.0
      soma=math.sqrt(soma)
      sys.stdout.write(str((float(splitted[0])-media)/soma))
      sys.stdout.write(' ' + str(soma))
      sys.stdout.write('\n')
  inFile.close()

if __name__ == '__main__':
  main()
