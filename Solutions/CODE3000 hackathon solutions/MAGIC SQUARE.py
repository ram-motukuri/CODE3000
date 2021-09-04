while(1):
    n=int(input())
    l = [[0] * n for p in range(n)]
    i=0
    j=(n-1)//2
    for k in range(1,(n*n)+1):
        if(i>=0 and j<n):
            if(l[i][j]!=0):
                i=i+2
                j=j-1
                l[i][j]=k
                i=i-1
                j=j+1
            else:
                l[i][j]=k
                i=i-1
                j=j+1
        elif(i<0 and j>n-1):
            i=i+2
            j=j-1
            l[i][j]=k
            i=i-1
            j=j+1
        elif(i<0):
            i=n-1
            l[i][j]=k
            i=i-1
            j=j+1
        elif(j>n-1):
            j=0
            l[i][j]=k
            i=i-1
            j=j+1
    for i in l:
        print("\t".join(list(map(str,i))))
    
