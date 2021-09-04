from math import factorial
def prime(n):
    n+=1
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]
def Fibonacci(n): 
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
def sum_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return sum(factors)
def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return len(factors)
def bin_diff(n):
    binary=[i for i in bin(n)[2:]]
    return abs(binary.count('0')-binary.count('1'))
def bin_sum(n):
    binary=[int(i) for i in bin(n)[2:]]
    return sum(binary)
num_cashews=int(input())
n=0
while(1):
    temp=[prime(n),Fibonacci(n),sum_all_factors(n),get_all_factors(n),factorial(n),bin_diff(n),bin_sum(n)]
    if(sum(temp)<num_cashews):
        num_cashews-=sum(temp)
        n+=1
    elif(sum(temp)==num_cashews):
        n+=1
        print(n)
        break
    else:
        total=0
        for i in range(len(temp)):
            if(total+temp[i]<num_cashews):
                total+=temp[i]
                num_cashews-=temp[i]
            else:
                print("Rounds served:",n)
                print("Cashews needed to serve",n+1,"round:",sum(temp[i:])-num_cashews)
                break
        break
