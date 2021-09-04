from collections import Counter
import math
import random
while(1):
    a=int(input())
    k=[]
    for i in range(a):
        #x=int(input())
        k.append(str(1))
    print(" ".join(k))
    k=list(map(int,k))
    b=int(input())
    t=0
    s=0
    x=0
    d=b//a
    b=b%a
    if(d>0):
        for i in range(d):
            k=list(map(lambda x: math.ceil(x/2),k))
    c=Counter(k).most_common()
    c.sort(reverse=True)
    for i in c:
        t=t+i[1]
        x=x+1
        if(t<=b):
            s=s+math.ceil(i[0]/2)*i[1]
        else:
            u=t-b
            v=i[1]-u
            s=s+(math.ceil(i[0]/2)*v)+i[0]*u
            break
    s=s+sum(list(map(lambda y: y[0]*y[1],c[x:])))
    print(s)
