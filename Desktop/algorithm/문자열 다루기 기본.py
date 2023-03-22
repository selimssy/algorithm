def solution():
    s = "a234"
    num = 0
    for i in range(len(s)):
        if (ord(s[i])>=48 and ord(s[i])<=57):
            num +=1
    print(num)
    if((len(s)==4 or len(s)==6) and num == len(s)):
        return True 
    else: 
        return False
    
print(solution())    