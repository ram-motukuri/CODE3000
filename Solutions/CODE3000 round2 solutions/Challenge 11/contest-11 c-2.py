'''from math import gcd 
from functools import reduce
import timeit
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
def lcm(denominators):
    return reduce(lambda a,b: a*b // egcd(a,b), denominators)
while(1):
    n=int(input())
    arr=[i for i in range(1,n+1)]
    start = timeit.default_timer()
    print(lcm(arr)+n*n)
    stop = timeit.default_timer()
    print(stop-start)'''


import timeit
def LCM2(last):
    factors = list(range(last+1))
    result = 1
    for n in range(last+1):
        if factors[n] > 1:
            result *= factors[n]
            for j in range(2*n, last+1, n):
                factors[j] //= factors[n]
    return result
#sieve();
while(1):
    n=int(input())
    start = timeit.default_timer()
    print(LCM2(n)+n*n)
    stop = timeit.default_timer()
    print(stop-start)
    

