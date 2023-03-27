n = 10



result = 0
    
for i in range(1, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        result += 1

    #print()
    #print(str(i) + " : 약수 " + str(cnt) + "개")    

#print()
print(result)    


print(sum([True, True, True, False]))