n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    l[i]=l[i]**2
l=sorted(l)
print(*l)
