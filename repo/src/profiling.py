##  @brief program that calculates the standard deviation from a sequence of numbers sepparated by white symbols
#   read from stdin.
#   @author Martin Pavella xpavel39

import sys

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
        data.append( int(num) )


#   constants used in calculation
data_len = len(data)
data_average = sum(data) / data_len

sum = 0;

for x in data:
    sum += (x**2)

res = sum - data_len * (data_average**2)
res = res * (1 / (data_len - 1))
res = sum ** 0.5

print(res)