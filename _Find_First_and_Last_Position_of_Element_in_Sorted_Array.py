n=int(input())
arr=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if(arr[i]==s):
        print(i,end=" ")
        x=i
        c+=1
if(c==1):
    print(x)
if(c==0):
    print(-1,-1)