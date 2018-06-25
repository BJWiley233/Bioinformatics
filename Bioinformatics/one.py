# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 23:34:58 2018

@author: bjwil
"""

# file one.py
def func():
    print("func() in one.py")

print("top-level in one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")