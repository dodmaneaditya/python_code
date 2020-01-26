'''
Author : Aditya Hegde
Description : Demo on importing a module, specific function from a module and renaming a function
Date : March 23rd, 2017
'''

import math  #Importing math module
#from math import factorial  # Importing specific function from a module
from math import factorial as fact # Renaming a function while importing from a module

x = 5
y = 3

#f = fact(x) / (fact(y) * fact(x-y)) #This will give float value
f = fact(x) // (fact(y) * fact(x-y)) #This will give integer value because we are using // integer division value
print(" \n Permutation Value:"+str(f)+"\n")
