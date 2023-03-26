k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]


score.sort(reverse=True)
amount = 0

for i in range(0,len(score)//m):
    amount += min(score[m*i : m*i+m]) * m
    print(min(score[m*i : m*i+m]))
print(amount)    