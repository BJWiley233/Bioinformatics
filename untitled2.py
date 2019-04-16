# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 05:54:57 2019

@author: bjwil
"""


import networkx as nx

sign = '->'


with open ('dataset_203_2.txt', 'r') as in_file:
    lines = in_file.read().split('\n')

edict = {}

for connection in lines:
    connection = connection.replace(" ", "")
    edict[connection.split('->')[0]] = [v for v in connection.split('->')[1].split(',')]


G = nx.DiGraph(edict)
euler = list(nx.eulerian_circuit(G))
path = euler[0][0] + sign + euler[0][1]
for line in euler[1:]:
    path = path + (sign + line[1])

with open('Output8.txt', 'w') as f:
        f.write(path)
        
import common