"""@package docstring
\file math.py
\brief Math package for calculator
This package contains declarations for math functions: +,-,*,/,!,^,^-1/x,... 
"""
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

