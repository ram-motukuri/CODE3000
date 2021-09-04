from collections import Counter
# Python program to print a hollow 
# inverted pyramid pattern 

def printPattern(n) : 
    for i in range(1,n+1) :
        for j in range(1,i) :
            print (" ",end="")
        for j in range(1,(n * 2 - (2 * i - 1))+1):
            if (i == 1 or j == 1 or j == (n * 2 - (2 * i - 1))):
                print (".", end="") 
            else :
                print(" ", end="") 
        print ("")

while(1):
    k=input().split(" ")
    p=int(input())
    k="".join(k)
    c=Counter(k)
    c=c.most_common()
    v=c[p-1][1]
    printPattern(v)
