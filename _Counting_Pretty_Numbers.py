T=int(input())
for i in range(T):
    L,R=[int(x) for x in input().split()]
    count=0
    for j in range(L,R+1):
        if(j%10==2 or j%10==3 or j%10==9):
            count+=1
    print(count)
