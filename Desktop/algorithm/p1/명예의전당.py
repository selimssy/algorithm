k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print([min(sorted(score[0:i+1], reverse=True)[0:k]) for i in range(len(score))])