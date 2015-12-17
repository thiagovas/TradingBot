#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

candles_path = '../../../data/allStocks/daily_candles/'
initial_capital = 1000000
initial_lot_size = 100
tests = 1000


from random import randint
import sys



def grep_year(line):
  return line[-1][:4]


def grep_opening_price(line):
  return float(line[1])


def run(all_lines, year):
  capital = initial_capital
  lot = initial_lot_size
  neg=0
  for x in all_lines:
    line = x.split(',')
    if grep_year(line) == str(year):
      r = randint(1, 100)
      price = grep_opening_price(line)
      if r > 50:
        # Buy
        capital -= lot*price;
        neg += lot 
      else:
        # Sell
        capital += lot*price
        neg -= lot
        
      if capital < 0:
        print 'DEU RUIM'
        sys.exit()
  
  
  # Closing position
  if neg > 0:
    # Have to sell everything
    capital += neg*price
  elif neg < 0:
    # Have to buy everything
    # I sum neg*price here because neg is negative
    capital += neg*price
  
  return capital


def main():
  year = input('Year: ')
  stock = raw_input('Stock: ')
  candles = open(candles_path+stock)
  all_lines = candles.readlines()
  
  result = 0
  for i in range(tests):
    ret = run(all_lines, year)
    result += ret
  print result/tests
  candles.close()

  


if __name__ == '__main__':
  main()
