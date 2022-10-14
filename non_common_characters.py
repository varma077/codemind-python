s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l=[]
for i in s1:
    if i not in s2:
        if i not in l:
            if i!=' ':
                l.append(i)
for i in s2:
    if i not in s1:
        if i not in l:
            if i!=' ':
                l.append(i)
a=sorted(l)
print("".join(a))