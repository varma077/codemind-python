n=int(input())
l=list(map(int,input().split()))
es=0
os=0
for i in range(0,n):
    if i%2==0:
        os+=l[i]
    else:
        es+=l[i]
if os-es==0:
    print("YES")
else:
    print("NO")
    
    