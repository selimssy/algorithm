from collections import Counter

weights = [100,180,360,100,270]
people = Counter(weights)
print(people)

pair = [1, 1.5, 2, (2/3), (4/3), 0.5, 0.75]
count = 0



for i in range(len(weights)-1):
    for j in range(i+1, len(weights)):
        if (weights[i] / weights[j]) in pair:
            #print("(" + str(weights[i]) + ", " + str(weights[j]) + ")")
            count += 1


a = weights.count([100,360])
print(a)

#print(count)