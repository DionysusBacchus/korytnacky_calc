##
# @file mathlib.py
# @author Jakub Sikula
#

from math import *
import re
import UI 
import signal

##
# 	@biref library which contains funcitons that evaluate and calculate math problems
#	Evaluation and calculation is based on calling of sumbit()



## Function for comunication with other scripts
#   @param  foo     to do
set_expr = None
def set_set_expr(foo):
    global set_expr
    set_expr = foo

##  Function which handles error in case of infite calucluation
#   @param  num     to do
#   @param  stack   to do
def timeout_handler(num, stack):
    raise Exception("Takes too long to calculate")
    

##  Function for root function
#   @param  x   root of number
#   @param  n   nth root
def sqrt(x,n=2):
    if x == 0:
        return 0
    if n == 0:
        raise ValueError
        set_expr("Neplatný vstup")
        return "CATCH"
    if isinstance(n,float):
        raise ValueError
        set_expr("Neplatný vstup")
        return "CATCH"
    if x < 0:
        if n%2 == 0:
            raise ValueError
            set_expr("Neplatný vstup")
            return "Neplatný vstup"
        else:
            ans = -(-x)**(1./n)

    else: 
        ans = x**(1/n)
    if isinstance(ans, complex):
        raise ValueError("Answer is complex number")
    else:
        return ans

##  Variable witch holds previous answer
Ans = 0

##  Function returns converted string to correct form
#   @param  string  data to be converted 
def convert(string):
    global Ans
    string = string.replace("√" ,"sqrt")
    string = string.replace("^","**")
    string = string.replace("x","*")
    string = string.replace("e","2.718281828459045")
    string = string.replace("π","3.141592653589793")
    string = string.replace("Ans",str(Ans))
    if "!" in string:
        string = re.sub(r'([0-9]+)!|([0-9]+\.[0-9]+)!|\((.+)\)!|\((.+)\)!|(^-[0-9]+)!|(^-[0-9]+\.[0-9]+)!',r'factorial(\1\2\3\4\5\6)',string)
    if "|" in string:
        string = re.sub(r'\|\((.+?)\)\||\|(.+?)\|',r'abs(\1\2)',string)
    if "sqrt" in string:
        string = re.sub(r'sqrt\(([\w]+)\)|sqrt(([\w]+))',r'sqrt(\1\2)',string)
    if "ln" in string:
        string = re.sub(r'ln(.+)',r'log(\1)',string)
    return string




##  Function returns calculated data in string and sets data to display
#   @param  string  data to evaluate and calculate
def submit(string):
    global Ans
    #print ("Previous ans= " + str(Ans))
    string = convert(string)
    if "CATCH" in string:
        set_expr("Neplatný vstup")
        return "Neplatný vstup"
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(8)
        try:
            answer = 0
            #print (string)
            answer = eval(string,globals())
            #print (answer)
        finally:
            signal.alarm(0)
    
    except ZeroDivisionError:
        set_expr("Nulou se nedá dělit")
        return "Nulou se nedá dělit"
    except SyntaxError:
        set_expr("Chyba syntaxe")
        return "Chyba syntaxe"
    except ValueError:
        set_expr("Neplatný vstup")
        return "Neplatný vstup"
    except NameError:
        set_expr("Chyba syntaxe")
        return "Chyba syntaxe"
    except TypeError:
        set_expr("Neplatný vstup")
        return "Neplatný vstup"
    except OverflowError:
        set_expr("Výsledek mimo maximálnej rozsah")
    except Exception:
        set_expr("Příliš komplikované")
    else:
        
        answer = ('%.15f' % float(answer)).rstrip('0').rstrip('.')
        #print (answer)
        set_expr(answer)
        Ans = answer
        #print (Ans)
        return float(answer)

##  Function returns the average vale of given data
#   @param  l   list holding the data
def avg(l):
    return sum(l) / len(l)

##  Function sums the squares of all given values
#   @param  l   list holding the data
def sum_squares(l):
    sum = 0
    for x in l:
        sum += (x ** 2)
    return sum
