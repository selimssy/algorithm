ingredient = [1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]

stack = []
count = 0

for item in ingredient:
    stack.append(item)
    
    if item == 1 and len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
        stack = stack[:-4]
        count += 1
    
print(count)