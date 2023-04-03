numbers = [2,2,3,3]
budget = 10


numbers.sort()
list = []
for i in range(0, len(numbers)):
    if sum(list) + numbers[i] <= budget:
        list.append(numbers[i])

print(len(list))