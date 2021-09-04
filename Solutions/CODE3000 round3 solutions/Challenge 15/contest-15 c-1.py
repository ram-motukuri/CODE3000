from functools import reduce
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]
while(1):
    n=int(input())
    l=primes1(n)
    k=int(input())
    x=len(l)
    s=[]
    for i in range(0,x,k):
        if(i+k<=x-1):
            y=reduce((lambda x, y: x * y), l[i:i+k])
            s.append(str(y))
        else:
            y=reduce((lambda x, y: x * y), l[i:])
            s.append(str(y))
    print(" ".join(s))


