s=input()
s=s.lower()
v="aeiou"
con="bcdfghjklmnpqrstvwxyz"
l=s.split()
c=0
for i in l:
    let=len(i)-1
    if(i[0] in v and i[let] in con):
        c+=1
print(c)