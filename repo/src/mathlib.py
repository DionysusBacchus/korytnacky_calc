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
import signal


## Function for comunication with other scripts
set_expr = None
def set_set_expr(foo):
    global set_expr
    set_expr = foo

##  Function which handles error in case of infite calucluation
def timeout_handler(num, stack):
    print ("Recived SIGALRM")
    set_expr("Příliš komplikované")
    raise Exception("Takes too long to calculate")
    

##  Constructor of root function 
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

##  Function which convert input string and returns edited string usable in evaluation
def convert(string):
    global Ans
    string = string.replace("√" ,"sqrt")
    string = string.replace("^","**")
    string = string.replace("x","*")
    string = string.replace("e","2.718281828459045")
    string = string.replace("π","3.141592653589793")
    string = string.replace("Ans",str(Ans))
    if "!" in string:
        string = re.sub(r'-([0-9]+.[0-9]+)!|([0-9]+.[0-9]+)!|([0-9]+)!|-([0-9.]+)!|\((.+?)\)!',r'factorial(\1\2\3)',string)
    if "|" in string:
        string = re.sub(r'\|\((.+?)\)\||\|(.+?)\|',r'abs(\1\2)',string)
    if "sqrt" in string:
        string = re.sub(r'sqrt\(([\w]+)\)|sqrt(([\w]+))',r'sqrt(\1\2)',string)
    return string




##  Function which is used to submit and convert
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
    else:
        
        answer = ('%.15f' % float(answer)).rstrip('0').rstrip('.')
        #print (answer)
        set_expr(answer)
        Ans = answer
        #print (Ans)
        return float(answer)


