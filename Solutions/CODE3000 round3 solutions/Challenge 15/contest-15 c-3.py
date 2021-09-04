def dup(car,seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(car[loc])
            start_at = loc
    return locs
while(1):
    x=int(input())
    name=[]
    car=[]
    price=[]
    cp={}
    for y in range(x):
        i=int(input())
        if(i==1):
            n=input()
            name.append(n)
            c=input()
            car.append(c)
            p=int(input())
            if c not in cp.keys():
                cp[c]=p
        if(i==2):
            n2=input()
            cars=dup(car,name,n2)
            oset=dict.fromkeys(cars).keys()
            cars=",".join(list(oset))
            print(cars)
        if(i==3):
            sc=sorted(cp.items(), key = lambda kv:(kv[1], kv[0]))
            sc1=[]
            for i in sc:
                sc1.append(":".join(list(map(str,list(i)))))
            sc1=",".join(sc1)
            print(sc1)
        if(i==4):
            c2=input()
            names=dup(name,car,c2)
            oset=dict.fromkeys(names).keys()
            names=",".join(list(oset))
            print(names)
        
        
