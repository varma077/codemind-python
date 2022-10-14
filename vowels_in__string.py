
s=input()
v="aeiouAEIOU"
l=[]
for i in range(len(s)):
    if s[i] in v and s[i] not in l:
        l.append(s[i])
print(*l)