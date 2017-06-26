#!/usr/bin/env python
# coding: utf-8
#
# This piece of code receives a bunch of filenames. Each file
# has data of a time series. Then, the code reads all series,
# join them and tries to fix any mismatch of dates, or any
# kind of error between the series.
#
# The output of this code is a file with all series joined into
# one file. Each line representing a day, following the schema:
#
# Date  [DR 1]  [CVaR 1]  [DR 2]  [CVaR 2] ... [DR N] [CVaR N]
#
# DR    = Daily Return
# DR _  = Daily Return of time series _
#
# Output file saved at "./treated" folder.


def main():
  pass



if __name__ == '__main__':
  main()
