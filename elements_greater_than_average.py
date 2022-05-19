t=int(input())
arr=list(map(int,input().split()))
su=sum(arr)
a=su//t
c=0
for i in arr:
    if(i>=a):
        c+=1
print(c)