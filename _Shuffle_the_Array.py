n=int(input())
arr=list(map(int,input().split()))
j=n//2
for i in range(n//2):
    if(j<n):
        print(arr[i],arr[j],end=" ")
    j+=1