import math

def countDiv(n) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
              
            # If divisors are equal, 
            # count only one 
            if (n / i == i) : 
                cnt = cnt + 1
            else : # Otherwise count both 
                cnt = cnt + 2 
    return cnt
 
n=int(input())
k=0
for i in range(1,n+1):
    if(i%countDiv(i)==0):
        k=k+i
print(k)
