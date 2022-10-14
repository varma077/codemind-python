a=int(input())
l=list(map(int,input().split()))
b=int(input())
y=max(l)
for i in range(a):
        if l[i]+b<y:
            print(False,end=' ')
        else:
            print(True,end=' ')