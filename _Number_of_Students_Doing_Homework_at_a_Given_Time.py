m=int(input())
st=list(map(int,input().split()))
n=int(input())
et=list(map(int,input().split()))
q=int(input())
c=0
for i in range(m):
    if  q>=st[i] and q<=et[i]:
        c+=1
print(c)