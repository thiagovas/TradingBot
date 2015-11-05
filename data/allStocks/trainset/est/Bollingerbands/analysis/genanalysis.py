#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Thiago Silva
# 
# 
# 

import sys

path='../'

def main():
  files = [ f for f in listdir(path) if (isfile(join(path, f)) and f[-5:]=='bands') ]
  for f in files:
    


if __name__ == '__main__':
  main()
