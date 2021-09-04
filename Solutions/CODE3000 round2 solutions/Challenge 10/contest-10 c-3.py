while(1):
    a=input()
    a=list(a)
    k=[]
    if(a.count(max(a))>1):
        a1=[i for i ,val in enumerate(a) if val==max(a)]
        for i in a1:
            k.append(a[i:])
        k.sort()
        print("".join(k[-1]))
    else:
        print("".join(a[a.index(max(a)):]))
