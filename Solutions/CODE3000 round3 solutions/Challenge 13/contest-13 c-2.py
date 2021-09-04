import math
def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b 
        n -= 1
    return a
if __name__ == "__main__":
    t=int(input())
    l=[]
    for n in range(t):
        k=int(input())
        l.append(k)
    p=[fib(i) for i in range(max(l)+1)]
    summ=0
    for k in range(len(l)):
        for i in range(1,l[k]+1):
            for j in range(i,l[k]+1):
                if(math.gcd(p[i],p[j])==1):
                    summ=summ+1
        print(summ)
        summ=0
