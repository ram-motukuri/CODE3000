from collections import deque
import random
def segment(k,arr):
    n=len(arr)
    ans=[]
    Qi = deque()
    for i in range(k):
        while Qi and arr[i] <= arr[Qi[-1]]:
            Qi.pop() 
        Qi.append(i); 
    for i in range(k, n):
        ans.append(arr[Qi[0]])
        while Qi and Qi[0] <= i-k: 
            Qi.popleft()  
        while Qi and arr[i] <= arr[Qi[-1]] : 
            Qi.pop() 
        Qi.append(i)
    ans.append(arr[Qi[0]])
    return max(ans)
while(1):
    t=int(input())
    arr=[]
    for i in range(t):
        u=random.randrange(1,100)
        arr.append(u)
    print(" ".join(list(map(str,arr))))
    x=int(input())
    result=segment(x,arr)
    print(result)
