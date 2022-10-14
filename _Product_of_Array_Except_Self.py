n=int(input())
arr=list(map(int,input().split()))
s=1
for i in range(n):
    s=1
    for j in range(n):
        if(i!=j):
            s*=arr[j]
    print(s,end=" ")