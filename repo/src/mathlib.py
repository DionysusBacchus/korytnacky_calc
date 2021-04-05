##@package
#\file math.py
#\brief Math package for calculator
#This package contains declarations for math functions: √,+,-,*,/,!,^,^-1/x,..., evalute function
#

##  
#

from math import *
import re

string = "-1*5-15"
def sqrt(x,n=2):
    return x**(1/float(n))

def convert(string):
    string = string.replace("√" ,"sqrt")
    string = string.replace("^","**")
    string = string.replace("e","2.718281828459045")
    string = string.replace("π","3.141592653589793")
    if "!" in string:
        string = re.sub(r'([\w+])!|\((.+?)\)!',r'factorial(\1\2)',string)
    if "|" in string:
        string = re.sub(r'\|\((.+?)\)\||\|(.+?)\|',r'abs(\1\2)',string)
    return string

def submit(string):
    string = convert(string)
    ans = eval(string)
    print (string)
    print (ans)
    
    #set_display_output(ans)
    return ans 


submit(string)