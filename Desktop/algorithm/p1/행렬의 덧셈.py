arr1 = [[1],[2]]
arr2 = [[3],[4]]
answer = []
print(answer)

for i in range(len(arr1)):
    answer.append([])
    for j in range(len(arr1[i])):
        answer[i].append(arr1[i][j] + arr2[i][j])

print(answer)        