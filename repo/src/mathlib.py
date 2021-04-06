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
    if "sqrt" in string:
        string = re.sub(r'sqrt\((.+?)\)|sqrt(.+?)',r'sqrt(\1\2)',string)
    return string


##  Variable witch holds previous answer
Ans = 0
##  Function which is used to submit and convert
def submit(string):
    string = convert(string)
    try:
        global Ans
        answer = 0
        answer = eval(string,globals())
    except ZeroDivisionError:
        window.set_expr("MathError")
    except SyntaxError:
        window.set_expr("SyntaxError")
    except ValueError:
        window.set_expr("MathError")
    else:
        window.set_expr(answer)
        Ans = answer
    return answer 


