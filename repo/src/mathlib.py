##@package
#\file math.py
#\brief Math package for calculator
#This package contains declarations for math functions: √,+,-,*,/,!,^,^-1/x,..., evalute function
#

##  
#

from math import *
#definitions = {'√':sqrt,'^': pow} 
string = "√2"   
def submit(string):
    string = string.replace("√" ,"sqrt")
    ans = eval(string)
    print (ans)
    #set_display_output(ans) 


submit(string)