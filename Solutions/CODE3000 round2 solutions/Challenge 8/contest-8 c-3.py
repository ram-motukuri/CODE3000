def Dragon_Curve_Sequence(n):  
    s = "1"
    for i in range(2, n + 1): 
        temp = "1"
        prev = '1'
        zero = '0'
        one = '1'
        for j in range(len(s)): 
            temp += s[j] 
            if (prev == '0'): 
                temp += one 
                prev = one 
            else: 
                temp += zero  
                prev = zero 
        s = temp 
    return s 
while(1):  
    n=int(input()) 
    s = Dragon_Curve_Sequence(n) 
    print(s)
