if __name__ == "__main__":
    n,w = map(int, input().split(" "))
    l = list(map(int, input().split(" ")))
    s=min([l[0],l[1]])
    v=max([l[0],l[1]])
    p=[]
    y=[]
    if(s!=v):
        while(v):
            s,v=v,s%v
        p.append(int(l[0]/s))
        p.append(s)
        for i in range(1,len(l)):
            a=l[i]/s
            p.append(int(a))
            s=a
        q=set(p)
        q=list(q)
        q=sorted(q)
        print(p)
        print(q)
        for i in p:
            y.append(chr(65+(q.index(i))))
        t=''.join(y)
        print("Case #"+str(x+1)+": "+str(t))
    else:
        for i in range(len(l)):
            if(l[i]!=l[i+1]):
                s=min([l[i],l[i+1]])
                v=max([l[i],l[i+1]])
                while(v):
                    s,v=v,s%v
                f=i
                if(f%2==0):
                    for i in range(f+1):
                        if(i%2==0):
                            p.append(int(l[i]/s))
                        else:
                            p.append(s)
                else:
                    for i in range(f+1):
                        if(i%2==0):
                            p.append(s)
                        else:
                            p.append(int(l[i]/s))
                p.append(s)
                for i in range(f+1,len(l)):
                    a=l[i]/s
                    p.append(int(a))
                    s=a
                q=set(p)
                q=list(q)
                q=sorted(q)
                for i in p:
                    y.append(chr(65+(q.index(i))))
                t=''.join(y)
                print("Case #"+str(x+1)+": "+str(t))
                break
            

        
            
        
                    
                
                
            
    
    
    
