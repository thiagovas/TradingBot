#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Converts the 15min candles to daily

from os import listdir, makedirs
from os.path import isfile, join, exists

min_candles_path = './15min_candles'
daily_candles_path = './daily_candles'


def get_date(value):
    ''' Given a line from a file, it returns the datetime '''
    return value[-1][:8]


def refresh_data(data, line):
    # codigo, Fechamento Atual, Abertura, Maximo, Minimo, Fechamento_anterior, negocios, quantidade_papeis, volume_financeiro, data
    ret=[]
    line=line.split(',')
    ret.append(line[0]) # Fechamento Atual
    ret.append(data[1]) # Abertura
    ret.append(str(max(float(data[2]), float(line[2]))))
    ret.append(str(min(float(data[3]), float(line[3]))))
    ret.append(line[4]) # Fechamento Anterior
    ret.append(str(float(line[5])+float(data[5])))
    ret.append(str(float(line[6])+float(data[6])))
    ret.append(str(float(line[7])+float(data[7])))
    ret.append(get_date(line))
    return ret


def new_data(line):
    line = line.split(',')
    ret = []
    for i in range(0, 8):
        ret.append(line[i])
    ret.append(get_date(line))
    return ret


def get_string_data(data):
    s=''
    for value in data:
        s+=value+','
    return s[:-1]+'\n'


def gen_daily_candle(filename):
    min_file = open(min_candles_path+'/'+filename, 'r')
    daily_file = open(daily_candles_path+'/'+filename, 'w')
    file_content = min_file.readlines()
    lastDate = ''
    data=[]

    for line in file_content:
        if get_date(line.split(',')) != lastDate:
            if lastDate != '':
                daily_file.write(get_string_data(data))
                data = new_data(line)
            else:
                data = new_data(line)    
        else:
            data = refresh_data(data, line)
        lastDate = get_date(line.split(','))
    daily_file.write(get_string_data(data))


def main():
    files = [ f for f in listdir(min_candles_path) if isfile(join(min_candles_path, f)) ]
    
    for f in files:
        if not exists(daily_candles_path):
            makedirs(daily_candles_path)
        
        gen_daily_candle(f)


if __name__ == '__main__':
    main()
