#print(7//2)
food = [1, 7, 1, 2]
answer = ''
for i in range(1,len(food)):
    answer += str(i)*(food[i]//2)

print(answer + "0" + answer[::-1])