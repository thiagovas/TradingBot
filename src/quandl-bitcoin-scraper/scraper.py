#!/usr/bin/env python
# coding: utf-8

import urllib2


def main():
  
  for year in range(2012, 2017):
    resp = urllib2.urlopen('https://www.quandl.com/api/v3/datasets/BITSTAMP/USD.csv?api_key=Uh1MZAHe9TJbR1tdDmSt&start_date='
                           + str(year) + '-01-02&end_date=' + str(year) + '-12-21')
    f = open('../../data/bitcoin/bitstampUSD-' + str(year), 'w')
    f.write(resp.read())
    f.close()


if __name__ == '__main__':
  main()
