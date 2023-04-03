s = "foobar"	

#print(s.index("a", -1))
#print(s.find("a"))

# 또 있을 경우
#a = [s.find() s.find(s[i], ) for i in range(len(s))]

#print(3 - s[::-1].find(s[3], 3))
#print("이전 인덱스 번호 : "  + str(    len(s)-(s[::-1].find(s[3], 3)+1)     ))
#i - len(s)-(s[::-1].find(s[i], len(s)-i)+1)

'''
for i in range(len(s)):
    #print("찾는 대상 : 인덱스 " + str(i) + "의 " + s[i])
    print("이전 인덱스 번호 : "  + str(    len(s)-(s[::-1].find(s[i], len(s)-i)+1)     ))
'''


# 문자열 반대로 해서 구하는법
answer = [-1 for _ in range(len(s))]
for i in range(len(s)):
    if s[::-1].find(s[i], len(s)-i) > -1: # 앞에 같은 글자 존재할 경우
        answer[i] = i  - (len(s)-(s[::-1].find(s[i], len(s)-i)+1))
print(answer)    




# 딕셔너리 사용법
answer = []
dic = dict()
for i in range(len(s)):
    if s[i] not in dic:
        answer.append(-1)
    else:
        answer.append(i - dic[s[i]])
    dic[s[i]] = i

print(dic)  # {'f': 0, 'o': 2, 'b': 3, 'a': 4, 'r': 5} 이런식으로 해당 문자가 마지막으로 언제 나왔는지 저장

