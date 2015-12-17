#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva

candles_path = '../../../data/allStocks/daily_candles/'
initial_capital = 1000000
initial_lot_size = 100


def grep_year(line):
  return line[-1][:4]


def grep_opening_price(line):
  return float(line[1])


def run(all_lines, year):
  pass


def main():
  
