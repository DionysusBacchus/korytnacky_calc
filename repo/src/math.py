##@package
#\file math.py
#\brief Math package for calculator
#This package contains declarations for math functions: +,-,*,/,!,^,^-1/x,... 

## Documentation for factorial funcion.
#
# Takes number as argument and returns calculated factorial of given number(n=3; returns=3*2*1).
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
## Documentation for add function
#
# Takes two numbers as arguments and return thier sum
def add(a,b):
	return a+b

## Documentation for sub function 
#
# Takes two numbers as arguments and return thier difference
def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

