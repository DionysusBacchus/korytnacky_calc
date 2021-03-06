##  @brief program that calculates the standard deviation from a sequence of numbers sepparated by white symbols
#   read from stdin.
#   @author Martin Pavella xpavel39

import sys
import mathlib

##  Function replaces runs of multiple space ' ' characters with exactly 1.
#   @param str string with source data
#   @return resulting string
def compact_spaces(str):
    res = ""
    first_space = True
    for c in str:
        if c != ' ':
            res += c
            first_space = True
        elif first_space:
            res += ' '
            first_space = False
    return res


#   read input data
data = []

for line in sys.stdin:
    line = line.strip().replace('\t',' ')
    line = compact_spaces(line).split(" ")

    for num in line:
    	if num != "":
		    data.append( float(num) )

data_len = len(data)
res = 0
if data_len != 0 and data_len != 1:
	data_average = mathlib.avg(data)

	#   calculation
	sum = mathlib.sum_squares(data)

	res = sum - data_len * (data_average**2)
	res = res * (1 / (data_len - 1))
	res = res ** 0.5
elif data_len == 1:
	res = data[0]

print(res)
