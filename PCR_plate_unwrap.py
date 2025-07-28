# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 17:18:43 2025

@author: willt
"""

with open(r"C:\Users\willt\SINC2_p6_pcr2.txt", 'r') as f:
    lines = f.readlines()

plate = [line.strip().split() for line in lines]

flat = [value for row in plate for value in row]

with open('SINC2_P6_PCR2_column.txt', 'w') as f:
    for value in flat:
        f.write(value + '\n')
