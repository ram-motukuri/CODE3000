import random
import time

def fun(a,b,n):
    #print(a,b,n)
    i = 0
    #print(i,n)
    swap = 0
    flip = 0
    while i<n:
        #print('happy')
        l = []
        if a[i]!=b[i]:
           # print('h1')
            l.append(i)
            j = i+1
            while j<n and len(l)>0:
                #print(j)
                if a[j]!=b[j]:
                    if a[j]==a[i]:
                        l.append(j)
                    elif a[j]!=a[i]:
                        temp = a[l[-1]]
                        a[l[-1]] = a[j]
                        a[j] = temp
                        swap+=1
                        l.pop()
                j+=1
            if len(l)!=0:
                flip+=len(l)
            i = j
        else:
            i+=1
    return (swap+flip )

n = int(input())
a = list(input())
b = list(input())
s1 = fun(a,b,n)
print(s1)
                
