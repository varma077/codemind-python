n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(j+i==n-1 or i==j):
            print("x",end="")
        else:
            print("0",end="")
    print()
    