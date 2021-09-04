def magle( n) :
    y = n - 1
    while(y >= 0) :
        i = 0
        while(i < y ):
            print(" ",end="")
            i = i + 1
        x = 0
        while(x + y < n ):
            if ((x & y) != 0) :
                print(" ", end = " ")
            else :
                print(". ", end = "")
            x =x + 1
        print()
        y = y - 1
		
while(1):
    n = int(input())
    magle(n)
