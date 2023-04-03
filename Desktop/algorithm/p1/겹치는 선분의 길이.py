lines = [[0, 5], [3, 9], [1, 10]]

position = []
for line in lines:
    position += list(range(line[0], line[1]))

print(position)


print(len(list(filter(lambda x: position.count(x) >=2 , set(position))))) 