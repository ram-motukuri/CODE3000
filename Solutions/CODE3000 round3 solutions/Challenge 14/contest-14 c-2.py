from bisect import bisect
from random import randint
while(1):
    x=int(input())
    k=[]
    for i in range(x):
        v=randint(0,10)
        print(v,end=" ")
        k.append(v)
    print(end="\n")
    p=sorted(k)
    t=[]
    for i in k:
        t.append(str(x-bisect(p,i)))
    print(" ".join(t))
