#This is a comment

#The following is the import section
#This brings in other python files that have pre-defined functions in them
#This will be present in every single program you write
from math import *
import numpy as np

#Here's how you can comment out multiple lines
"""
import time
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
from psm_plot import *
from random import *
from time_step_scrolling import *
"""
#The following is a sort of "global" area this code will execute first and will always execute


print("test")

#Below is a function definition
def main():
    #Notice the indentations... these are used in python rather than things like { }
    print("test")
    #Note the above line may or may not be executed

    #define a variable
    integer1 = 2
    print(integer1)

    float1 = 1.0
    print(float1)
    print("%5.2f" % float1)

    tmp = float1/integer1

    integer2 = 3
    print(tmp)
    print(integer1/integer2)

    print((int)(integer1/integer2))

    float2 = 3.0
    test = float1/float2 - 1e-12*float1/float2/1e-12
    print(test)

    #do a calculation
    #test2 = pow(float2,3.0)
    #print(test2)
"""
    #do some logic
    if(integer1>integer2):
     #   print("%d is larger than %d" % integer1, integer2)
    #else:
    #    print("%d is larger than %d" % (integer2, integer1))

    if(float2 > float1 and integer2 > integer1):
#        print("%d is larger than %d and %3.2f is larger than %3.2f" % (integer2, integer1,float2,float1))

    if(integer1<integer2):
 #       print("%d is smaller than %d" % (integer1, integer2))
    elif(float1<float2):
  #      print("%3.2f is smaller than %3.2f" % (float1, float2))
    else:
        "None of the above"

"""





    #do a loop



if __name__ == '__main__':
    main()











