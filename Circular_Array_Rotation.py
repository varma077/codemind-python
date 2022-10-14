n,ro,q=map(int,input().split())
arr=list(map(int,input().split()))
b=[]
for i in range(q):
    v=int(input())
    b.append(v)
x=v=0
while(ro>0):
    x=arr[0]
    arr[0]=arr[n-1]
    for i in range(1,n):
        v=arr[i]
        arr[i]=x
        x=v
    ro-=1
j=0
z=0
for i in range(n):
    if(j<len(b)):
        z=b[j]
        print(arr[z])
    j+=1