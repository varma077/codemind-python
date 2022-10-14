t=int(input())
for i in range(t):
    c=1
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            c+=1
    print(c)