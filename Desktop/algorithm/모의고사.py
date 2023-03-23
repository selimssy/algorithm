
answers = [1,2,3,4,5,1,2,3,4,5]	

result = {}
pattern_list = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
for i in range(3):
    idx = 0
    for j in range(len(answers)):
        if answers[j] == pattern_list[i][j % len(pattern_list[i])]:
            idx +=1 
    result[i+1] = idx 
    
res = list(filter(lambda x: result[x] == max(result[1], result[2], result[3]), result))
print(res)




