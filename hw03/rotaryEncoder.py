#!/usr/bin/env python3

# Program testing the rotary encoders
import time

left = '1'
right = '2'

ms = 100
maxCount = '1000000'

def init(eQep):
    counterpath = '/dev/bone/counter/'+eQep+'/count0'

    with open(counterpath+'/ceiling', 'w') as f:
        f.write(maxCount)
    
    with open(counterpath+'/enable', 'w') as f:
        f.write('1')

    return counterpath

c1 = init(left)
c2 = init(right)

f1 = open(c1+'/count', 'r')
f2 = open(c2+'/count', 'r')

olddata = -1
olddata2 = -1
while True:
    f1.seek(0)
    f2.seek(0)

    data = f1.read()[:-1]
    if data != olddata:
        olddata = data
        print("data1 = " + data)
        
    data = f2.read()[:-1]
    if data != olddata2:
        olddata2 = data
        print("data2 = " + data)

    time.sleep(ms/1000)
