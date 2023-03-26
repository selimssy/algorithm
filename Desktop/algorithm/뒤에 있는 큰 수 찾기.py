numbers = [2, 2, 2, 2]


except_last  = [list(filter(lambda x: x>numbers[i], numbers[numbers.index(numbers[i])+1:]))[0] if len(list(filter(lambda x: x>numbers[i], numbers[numbers.index(numbers[i])+1:]))) >0 else -1 for i in range(len(numbers)-1) ]
total = except_last + [-1]

print(total)