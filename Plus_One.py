n=int(input())
p=list(map(int,input().split()))
c=0
d=0
s=0
r=0
k=0
b=[]
for i in range(n):
    s=s*10+p[i]
r=s+1
j=0
while r>0:
    v=r%10
    b.append(v)
    r=r//10
    j+=1
    c+=1
for k in range(c-1,-1,-1):
    print(b[k],end=" ")