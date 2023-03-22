s = "Z"
n = 1

answer = ''
for i in range(len(s)):
    if s[i].isspace():
        answer += " "
    else:
        num = ord(s[i])+n
        if((ord(s[i]) >= 97 and ord(s[i]) <= 122 and num > 122) or (ord(s[i]) >= 65 and ord(s[i]) <= 90 and num > 90)):
            num = num-26
        answer += chr(num)        
print(answer)        