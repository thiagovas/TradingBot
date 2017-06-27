#!/usr/bin/env python
# coding: utf-8
#
# This script gets a DAT file and returns another DAT file with the
# formats of BLIP ( http://blip.idsia.ch/jobs/formats/ ).


from sys import argv


def main():
  if len(argv) != 3:
    print "Error:"
    print "Usage: python", argv[0], " [input filename] [output filename]"
    return
  
  
  fin = open(argv[1], 'r')
  fout = open(argv[2], 'w')
  all_lines = []
  cardinalities = []
  first_line = True
  for l in fin.readlines():
    splitted_line = l.split(' ')
    if splitted_line[-1] == '\n':
      splitted_line = splitted_line[:-1]
    
    splitted_line = splitted_line[1:]
    all_lines.append(splitted_line)
    if not first_line:
      int_list = [ int(x) for x in all_lines[-1] ]
      for i in range(len(cardinalities)):
        cardinalities[i] = max(cardinalities[i], int_list[i])
    else:
      cardinalities = [ 0 for x in all_lines[0] ]
    first_line = False
  
  
  # Number of variables.
  fout.write(str(len(all_lines[0])))
  fout.write('\n')
  
  # Names of each variable.
  first_line = True
  for name in all_lines[0]:
    if not first_line:
      fout.write(" ")
    fout.write(str(name))
    first_line = False
  fout.write('\n')
  
  # Variables cardinalities
  for x in cardinalities:
    fout.write(str(x+1) + " ")
  fout.write('\n')
  
  # Number of datapoints
  fout.write(str(len(all_lines)-1))
  fout.write('\n')
  
  # List of datapoints
  for i in range(1, len(all_lines)):
    for name in all_lines[i]:
      fout.write(str(name) + " ")
      first_line = False
    fout.write('\n')
   



if __name__ == '__main__':
  main()
