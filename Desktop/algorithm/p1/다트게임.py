s = "1S2D*3T"

sum = 0
l_index = []  # 영문자를 저장할 리스트
for i in range(len(s)):
    if s[i].isalpha(): 
        l_index.append(i)

bonus = {"S":1, "D":2, "T":3}        
option = {"*":2, "#":-1}

def score(i):
    n = int(s[l_index[i]-1]) if not s[l_index[i]-2].isdigit() else 10 
    b = bonus[s[l_index[i]]]
    next_idx = l_index[i]+1
    if next_idx < len(s) and s[next_idx] in option:
        o = option[s[next_idx]]
        '''
        if i > 0 and s[next_idx] == "*":
            score(i-1)
        '''    
    else:
        o = 1   
    global sum    
    print()
    print("n = " + str(n) + ", b = " + str(b) + ", o = " + str(o) + " | 점수 : " + str((n ** b) * o))
    return (n ** b) * o


for i in range(3):        
    sum += score(i)
    if i > 0 and l_index[i]+1 < len(s) and s[l_index[i]+1] == "*":
            sum += score(i-1)  

print(sum)    