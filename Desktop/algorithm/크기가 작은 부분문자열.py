t = "3141592"
p = "271"

#nums3 = [int(str3[i]) for i in range(len(str3))]


# lambda 사용
partial = [int(t[i:i+len(p)]) for i in range(len(t)-(len(p)-1))]
print(len(list(filter(lambda x: x<= int(p), partial))))


# if 사용해서 리스트 생성  -- 이게 더 간단한듯?
res = [int(t[i:i+len(p)]) for i in range(len(t)-(len(p)-1)) if int(t[i:i+len(p)]) <= int(p)]
print(res)