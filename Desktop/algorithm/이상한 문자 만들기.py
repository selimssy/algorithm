s = " try hello world"
s=s.lower()
idx = -1
for i in range(len(s)): 
    idx+=1
    if s[i].isspace():
        idx = -1
    if idx % 2 == 0:
        s = s[:i] + s[i].upper() + s[i+1:]      
print(s)