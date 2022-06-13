#dublicate character remove

a="My Name is Dipak"
s=""
for i in a:
    if i in s:
        continue
    else:
        s+=i
print(s)