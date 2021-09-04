def nthTerm(N): 
    nth = 0
    # Finding nth term 
    for i in range(N, 0, -1): 
        nth += pow(i, i) 
    return nth 
# Driver code
N = int(input())
print(nthTerm(N)) 
