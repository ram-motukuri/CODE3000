n=int(input())
k=list(map(int,input().split(" ")))
distk=set(k)
newk=set()
newk.add(min(k))
x=k.index(min(k))
ans=str(x)
if(len(k)==1):
    print(0)
else:
    i=0
    while(1):
        i=i+1
        if(newk!=distk):
            if(i%2!=0):
                if(x+1<=len(k)):
                    y=list(set(k[x+1:])-newk)
                    if(y!=[]):
                        y=max(list(set(k[x+1:])-newk))
                        #print(y,k[x+1:])
                        x=x+(k[x+1:].index(y))+1
                        #print(x,k[x],newk)
                        if(k[x] not in newk):
                            newk.add(k[x])
                            ans=ans+str(x)
                            #print(newk,ans)
            else:
                if(x>=0):
                    y=list(set(k[:x])-newk)
                    #print(list(set(k[:x])-newk))
                    if(y!=[]):
                        y=min(list(set(k[:x])-newk))
                        #print(y,k[:x])
                        x=k.index(y)
                        #print(x,k[x],newk)
                        if(k[x] not in newk):
                            newk.add(k[x])
                            ans=ans+str(x)
                            #print(newk,ans)
        else:
            print(ans)
            break

                    
            
        
