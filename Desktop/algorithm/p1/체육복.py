n = 3
lost = [3]	
reserve = [1]



0
# 양쪽 다 있는걸 먼저 해줘야ㅠㅠ 이거부터 다시하자~

#교집합
length = len(lost)
inter = set(lost)&set(reserve)
lost = list(set(lost).difference(inter))
reserve = list(set(reserve).difference(inter))
cnt = len(inter)

for i in lost:
    if (i-1) in reserve:
        cnt +=1
        reserve.remove(i-1)
    elif (i+1) in reserve:
        cnt +=1
        reserve.remove(i+1)
   
print(n - length + cnt) 



