k=list(map(int,input().split()))
l=list(map(int,input().split()))
count=0
su=0
for i in range(len(k)):
    if k[i]>l[i]:
        count+=1
    elif k[i]<l[i]:
        su+=1
print(count,su)