#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:14:07 2019

@author: Natalie
"""

def find_range(numbers):
    return max(numbers) - min(numbers)

def calc_mean(data):
    return sum(data)/len(data)

def calc_mode(data):
    numcount = []
    for data_point in data:
        count(data)
    return max(numcount)

def calc_median(data):
    if len(data)%2:
        return data[len(data)//2]
    else: 
        x = len(data)//2
        return(data[x] + data[x-1])/2