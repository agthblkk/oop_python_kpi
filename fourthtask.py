import argparse
from curses import KEY_REPLACE
parser = argparse.ArgumentParser()
parser.add_argument('W', type=int)
parser.add_argument('w', nargs = '+', type=int)
parser.add_argument('n', type=int)
args = parser.parse_args()

table = [[0 for i in range(args.W + 1)] for j in range(args.n + 1)]

for k in range(args.W):
    table[0][k] = 0

l = list(args.w)
def maxfromcells(n, prevEl, curEl):
    if(curEl + n < prevEl):
        return prevEl
    else:
        return curEl+n

l = list(args.w)
for col in range(args.W + 1):
    for row in range(args.n + 1):
        n = col - table[col][row]
        if(l[row] > row):
            table[col][row] = table[col][row-1]
        else:
            table[col][row] = maxfromcells(n, table[col - 1][row], l[row])
print(table)
        

 
# wt = [10, 20, 30] w
# W = 50 W
# n = len(val) 



