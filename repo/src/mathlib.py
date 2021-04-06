##@package
#\file math.py
#\brief Math package for calculator
#This package contains evaluation and calculating of string input from UI 
#

##  
#

from math import *
import re
import UI 


#string = "√(-8,3)"

##  Constructor of root function 
def sqrt(x,n=2):
    if x == 0:
        return 0
    if x < 0:
        ans = -(-x)**(1./n)
    else: 
        ans = x**(1./n)
    if isinstance(ans, complex):
        raise ValueError("Answer is complex number")
    else:
        return ans

##  Function which convert input string and returns edited string usable in evaluation
def convert(string):
    string = string.replace("√" ,"sqrt")
    string = string.replace("^","**")
    string = string.replace("x","*")
    string = string.replace("e","2.718281828459045")
    string = string.replace("π","3.141592653589793")
    if "!" in string:
        string = re.sub(r'([\w+])!|\((.+?)\)!',r'factorial(\1\2)',string)
    if "|" in string:
        string = re.sub(r'\|\((.+?)\)\||\|(.+?)\|',r'abs(\1\2)',string)
    return string

##  Function which is used to submit and convert 
def submit(string):
    string = convert(string)
    ans = eval(string)
    #print (string)
    #print (ans)
    window.set_expr(ans)
    return ans 

window = UI.UI()
window.set_submit_callback(submit)
window.start_loop()

#submit(string)