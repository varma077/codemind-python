a=int(input())
l=list(map(int,input().split()))
count=0
ma=0
for i in range(a):
    for j in range(a):
        if(l[i]==l[j]):
            count+=1
    if count>ma:
        ma=count
        x=l[i]
    elif count==ma:
        if x<l[i]:
            x
        else:
            x=l[i]
            
    count=0
print(x)