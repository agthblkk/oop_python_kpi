import argparse
import math 
import operator
parser = argparse.ArgumentParser()
parser.add_argument('operator', type=str)
parser.add_argument('x', type=int)
parser.add_argument('y', type=int)
args = parser.parse_args()

find = getattr(math, args.operator, None)
if (find):
    res = getattr(math, args.operator)
else:
    res = getattr(operator, args.operator)
print(res(args.x, args.y))
