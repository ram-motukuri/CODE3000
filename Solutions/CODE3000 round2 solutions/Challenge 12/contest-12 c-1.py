while(1):
    n=list(map(int,list(str(int(input())))))
    k=""
    for i in range(len(n)-1):
        k=k+str(n[i]^n[i+1])
    print(k)
