import argparse
parser = argparse.ArgumentParser()
parser.add_argument('x', type=int)
parser.add_argument('operator', type=str)
parser.add_argument('y', type=int)
args = parser.parse_args()
def prints(x, y, operator):
    if(operator == '+'):
        return x+y
    if(operator == '-'):
        return x-y
    if(operator == 'x'):
        return x*y
    if(operator == '/'):
        return x/y
print(prints(args.x, args.y, args.operator))

