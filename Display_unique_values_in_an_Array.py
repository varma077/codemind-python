n=int(input())
l=list(map(int,input().split()))
b=[]
s=0
for i in l:
    c=l.count(i)
    if c==1:
        b.append(i)
        s+=1
if s==0:
    print("-1")
else:
    print(*b)