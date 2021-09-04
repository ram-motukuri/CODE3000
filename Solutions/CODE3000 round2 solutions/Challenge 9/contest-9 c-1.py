import time
from collections import Counter
def SieveOfEratosthenesL(n,k):  
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    pr=[]
    for p in range(2, n): 
        if prime[p]: 
            pr.extend(list(str(p)))
    t=set(pr)
    v=[]
    for i in t:
        v.append([int(i),pr.count(i)])
    v.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    #c=Counter(pr)
    #c=c.most_common()
    return v[k-1][0]
def SieveOfEratosthenesC(n,k):  
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    pr=[]
    for p in range(2, n): 
        if prime[p]: 
            pr.extend(list(str(p)))
    c=Counter(pr)
    c=c.most_common()
    return c[k-1][0]
while(1):
    num=int(input())
    k=int(input())
    start = time.time()
    print("List : ",SieveOfEratosthenesL(num+1,k))
    print(time.time() - start)
    start = time.time()
    print("Counter : ",SieveOfEratosthenesC(num+1,k))
    print(time.time() - start)
