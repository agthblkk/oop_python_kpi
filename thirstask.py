import argparse
parser = argparse.ArgumentParser()
parser.add_argument('x', type=str)
args = parser.parse_args()
listnew = []
listone = list(args.x)
listnew1 = []
sum = 0
boolean = True
def number(m):
    b = False
    listnum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in range(0, len(listnum)):
        if (m == listnum[i]):
            b = True
    return b
for j in range(0, len(listone)):
    if(j%2 == 0):
        if(number(listone[j])):
            listnew.append(int(listone[j]))
        else:
            boolean = False
    else:
        if(number(listone[j])):
            listnew.append(int(listone[j]))
        else:
            listnew1.append(listone[j])
if(listnew1 == []):
    sum = ''
    for a in range(0,len(listnew)):
        sum = sum + str(listnew[a])
else:
    sum = listnew[0]
    if (boolean):
        for n in range(0, len(listnew1)):
            if(listnew1[n] == '+'):
                sum = sum + listnew[n+1]
            if(listnew1[n] == '-'):
                sum = sum - listnew[n+1]
            if(listnew1[n] == 'x'):
                sum = sum * listnew[n+1]
            if(listnew1[n] == '/'):
                sum = sum / listnew[n+1]
    else:
        sum = 'None'
print(boolean,',',sum)