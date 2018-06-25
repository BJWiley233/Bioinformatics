# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 20:44:28 2018

@author: bjwil
"""
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
genome = readGenome('Vibrio_cholerae.txt')
len(genome)
first_String = 'ACAACTATGCATACTATCGGGAACTATCCT'
first_String.count('ACTAT')

nStr = 'CGATATATCCATAG'
pattern = 'ATA'

count =0
flag=True
start=0
while flag:
    a = nStr.find(pattern,start)  # find() returns -1 if the word is not found, 
                                  #start i the starting index from the search starts(default value is 0)
    if a==-1:          #if pattern not found set flag to False
        flag=False
    else:               # if word is found increase count and set starting index to a+1
        count+=1        
        start=a+1
print(count)
nStr.count(pattern)

import re
def occurrences(text, sub):
        return len(re.findall('(?={0})'.format(re.escape(sub)), text))
occurrences(nStr,pattern)


code = 'AAAACCCGGT'
len(code)


def Reverse(string):
    rev = ''
    for i in range(len(string), 0, -1):
        rev += string[i-1]
    complement = ''
    for i in range(0,len(rev)):
        if rev[i] == 'A':
            complement += 'T'
        elif rev[i] == 'C':
            complement += 'G'
        elif rev[i] == 'G':
            complement += 'C'
        elif rev[i] == 'T':
            complement += 'A'
    return complement

len(code)
len(Reverse(code))
import os
os.path.expanduser('~')

a = []

import numpy
numpy.sum(a)
print(*a, sep = ' ')
print(subString, sep = ' ')

def pointFunction(inputString,subString):
    array = []
    for i in range(0,len(inputString)):
        if subString == inputString[i:len(subString)+i]:
            array.append(i)
    print(*array)
    '''return array'''
inputString = readGenome('dataset_3_5 (1).txt')
pointFunction(inputString,'GATCGACGA')

target_url = 'http://bioinformaticsalgorithms.com/data/realdatasets/Rearrangements/E_coli.txt'
import urllib.request
data = urllib.request.urlopen(target_url)

def readAll(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            genome += line.rstrip()
    return genome
newData = readAll(data)
import urllib.request

req = urllib.request.Request('https://stepik.org/media/attachments/lessons/3/Vibrio_cholerae.txt')
with urllib.request.urlopen(req) as response:
   the_page = response.read().rstrip()
   if isinstance(the_page, bytes):
      the_page = the_page.decode('utf-8')
   
len(the_page)
the_page[-5:]
by = bytes
string = the_page[0:20]
isinstance(string, by)

b = b.decode('utf-8')

pointFunction(the_page,'CTTGATCAT')
