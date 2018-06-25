# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 23:40:32 2018

@author: bjwil
"""

import one

print("top-level in two.py")
one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")