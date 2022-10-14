n,m=map(int,input().split())
s=0
arr=[list(map(int,input().split())) for i in range(n)]
for j in range(n):
    for k in range(m):
        s=s+arr[j][k]
print(s)