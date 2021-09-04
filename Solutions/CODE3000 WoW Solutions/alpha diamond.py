import string
n = int(input())
a=string.ascii_lowercase
l=[]
w=4*n-3
for i in range(n):
    b='-'.join(a[i:n])
    l.append((b[::-1]+b[1:]).center(w,'-'))
print("\n".join(l[::-1]+l[1:]))
