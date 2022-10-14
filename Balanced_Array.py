t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        c=sum(a[:i])
        d=sum(a[i+1:])
        if(c==d):
            count=1
            break
    if count==1:
        print("YES")
    else:
        print("NO")
