a=int(input())
s=input()
c=0
for i in s:
    if i=='.':
        
        c+=1
if(c>a//2):
    print("YES")
    for i in s:
        if( i=='.'):
            print("B",end="")
        else:
            print(i,end="")
else:
    print("NO")