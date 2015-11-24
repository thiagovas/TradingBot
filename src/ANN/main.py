#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autor__= 'Thiago Silva'


import datareader
import neuralnetwork 


interval_days = 0
interval_days_options=[5, 7, 10, 15, 21]


def readintervaldays():
  while True:
    try:
      interval_days = int(input('Interval days: '))
      if not interval_days in interval_days_options:
        raise NameError
      break
    except NameError:
      print 'Input just 5, 7, 10, 15 or 21'


def main():
  readintervaldays()

if __name__ == '__main__':
  main()
