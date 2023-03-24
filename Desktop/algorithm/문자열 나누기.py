s = "acaaaaaa"
result = 0
idx = 0
score = 0

for i in range(len(s)):
    if s[i] == s[idx]:
        score +=1
    else:
        score -=1
        if score == 0:
            result +=1
            idx = i+1
            score = 0
if score > 0:
    result +=1

print(result)
