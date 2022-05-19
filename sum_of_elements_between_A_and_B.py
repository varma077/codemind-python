t=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
su=0
for i in arr:
    if(i>=a and i<=b):
        su+=i
print(su)