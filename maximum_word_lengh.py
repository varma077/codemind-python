s=input()
l=s.split()
max=0
for i in l:
    if(len(i)>max):
        max=len(i)
print(max)