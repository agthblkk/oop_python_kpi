import argparse
from re import M
parser = argparse.ArgumentParser()
parser.add_argument('W', type=int)
parser.add_argument('w', nargs = '+', type=int)
parser.add_argument('n', type=int)
args = parser.parse_args()

table = [[0 for i in range(args.W + 1)] for j in range(args.n + 1)]

for k in range(0, args.W + 1):
    table[0][k] = 0

l = list(args.w)
l.insert(0, 0)

m = 0
l1 = 0
def maxfromcells(m, prevEl):
    if(m < prevEl):
        return prevEl
    else:
        return m
for row in range(1, args.n + 1):
    for col in range(args.W + 1):
        m = col - l[row]
        if(l[row] <= col):
            l1 = l[row] + table[row-1][m]
            table[row][col] = maxfromcells(l1, table[row-1][col])
        else:
            table[row][col] = 0
print(table[row][col])




