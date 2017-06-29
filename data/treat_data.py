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
# Date  [DR 1_1]  [VaR 1_1]  [DR 1_2]  [VaR 1_2]  [DR 2_1]  [VaR 2_1] ... [DR N_K] [VaR N_K]
#
# DR    = Daily Return
# DR N_K  = Daily Return of time series N lagged of K days
# VaR calculated at 5%, and it's saved in logarithmic scale.
#
# Output file saved at "./treated" folder.


import math
from sys import argv
from math import log, fabs
from scipy.stats import norm
import numpy as np



def get_full_ts(ts):
  '''
    TODO(thiagovas): Write Me
  '''
  r_ts = {}
  n_days = 5
  v_tmp = []
  for key in sorted(ts):
    value = ts[key]
    v_tmp.extend(value)
    
    if len(v_tmp) > n_days*2:
      v_tmp = v_tmp[:-2]
    
    if len(v_tmp) < n_days*2:
      continue
    
    r_ts[key] = v_tmp
  
  return r_ts 
  


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

  tmp = 1
  r_ts = {}
  returns = []
  for key in sorted(ts):
    value = ts[key]
    returns.append(float(value-tmp)/tmp)
    if len(returns) < 30:
      tmp = value
      continue
    
    if len(returns) > 90:
      del returns[0]
    mu = np.mean(returns)
    sigma = np.std(returns)
    valueAtRisk = log(norm.ppf(0.05, mu, sigma)+1000)

    neue_key = key

    if neue_key[0] == "\"" or neue_key[0] == "\'":
      neue_key = neue_key[1:]

    if neue_key[-1] == "\"" or neue_key[-1] == "\'":
      neue_key = neue_key[:-1]
 
    if not math.isnan(valueAtRisk):
      r_ts[neue_key] = [returns[-1], valueAtRisk]
    tmp = value

  return get_full_ts(r_ts)



def join_ts(main_ts, other_ts):
  '''
    TODO(thiagovas): Write Me
  '''
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
  '''
    TODO(thiagovas): Write Me
  '''
  ofile = open(output_filename, 'w')

  for key in sorted(joint_ts):
    value = joint_ts[key]
    ofile.write(key)
    for v in value:
      ofile.write(" " + str(v))
    ofile.write("\n")
  ofile.close()


def write_bayesian_output(bayesian_output_filename, joint_ts):
  '''
    TODO(thiagovas): Write Me
  '''
  ofile = open(bayesian_output_filename, 'w')

  for key in sorted(joint_ts):
    value = joint_ts[key]
    ofile.write("0 qid:12")
    cur_id = 1
    for v in value:
      ofile.write(" ")
      ofile.write(str(cur_id) + ":")
      ofile.write(str(v))
      cur_id += 1
    ofile.write("\n")
  ofile.close()


def main():
  if len(argv) == 1:
    print "Error: Inform at least one filename."
    return

  joint_ts = None
  output_filename = "./treated/joint"
  bayesian_output_filename = "./treated/joint_bayesian"
 
  fs = argv
  fs = fs[1:]
  
  for filename in fs:
    input_file = open(filename, 'r')
    ts = read_ts(input_file)
    joint_ts = join_ts(joint_ts, ts)
  
  write_output(output_filename, joint_ts)
  write_bayesian_output(bayesian_output_filename, joint_ts)



if __name__ == '__main__':
  main()
