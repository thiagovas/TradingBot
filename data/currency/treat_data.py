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
# Date  [DR 1]  [VaR 1]  [DR 2]  [VaR 2] ... [DR N] [VaR N]
#
# DR    = Daily Return
# DR _  = Daily Return of time series _
# VaR calculated at 5%.
#
# Output file saved at "./treated" folder.


from sys import argv
from scipy.stats import norm
import numpy as np



def read_ts(input_file):
  '''
    Function that, basically, reads a file and gets the date and
    the adjusted close price.

    It Returns a dictionary of dates and daily returns.
  '''
  first_line = True
  
  ts = {}
  for l in input_file.readlines():
    if first_line:
      first_line = False
      continue
    l = l.split(',')
    try:
      ts[l[0]] = float(l[-1])
    except ValueError:
      continue

  tmp = 0
  r_ts = {}
  returns = []
  for key in sorted(ts):
    value = ts[key]
    returns.append(value-tmp)
    if len(returns) > 90:
      del returns[0]
    mu = np.mean(returns)
    sigma = np.std(returns)
    valueAtRisk = norm.ppf(0.05, mu, sigma)
    
    neue_key = key
    
    if neue_key[0] == "\"" or neue_key[0] == "\'":
      neue_key = neue_key[1:]
    
    if neue_key[-1] == "\"" or neue_key[-1] == "\'":
      neue_key = neue_key[:-1]
    
    r_ts[neue_key] = [value-tmp, valueAtRisk]
    tmp = value
  
  return r_ts



def join_ts(main_ts, other_ts):
  if main_ts == None:
    return other_ts
  
  tmp_ts = main_ts
  joint_ts = {}
  
  for key, value in other_ts.items():
    if key in tmp_ts:
      tmp_ts[key].extend(value)
  
  for key, value in tmp_ts.items():
    if key in other_ts:
      joint_ts[key] = value
  
  return joint_ts
  

def write_output(output_filename, joint_ts):
  ofile = open(output_filename, 'w')
  
  for key in sorted(joint_ts):
    value = joint_ts[key]
    ofile.write(key)
    for v in value:
      ofile.write(" " + str(v))
    ofile.write("\n")


def main():
  if len(argv) == 1:
    print "Error: Inform at least one filename."
    return
	
  joint_ts = None
  output_filename = "./treated/joint"
  
  fs = argv
  fs = fs[1:]
  
  for filename in fs:
    input_file = open(filename, 'r')
    ts = read_ts(input_file)
    joint_ts = join_ts(joint_ts, ts)
  
  write_output(output_filename, joint_ts)  
	


if __name__ == '__main__':
  main()
