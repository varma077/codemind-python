n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(j==0 or i==n-1 or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()