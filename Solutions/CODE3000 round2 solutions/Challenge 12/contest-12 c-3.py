from itertools import product
n=int(input())
s=input().split(" ")
t=s.count("?")
j=0
for x in range(1,n+1):
    for i in product('abcdefghijklmnopqrstuvwxyz',repeat=x):
        p=''.join(i)
        if j<t:
            if p not in s:
                print(p)
                j=j+1
        else:
            break
    break

    
        
