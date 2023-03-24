X = "100"	
Y = "203045"

answer = ""
'''
d1 = {char: X.count(char) for char in X}
d2 = {char: Y.count(char) for char in Y}
print(d1) # {'1': 2, '2': 2, '3': 1}
print(d2) # {'4': 1, '2': 1, '5': 1, '3': 1, '1': 1}
common_key = set(d1.keys()) & set(d2.keys())
'''

list1 = list(X)
list2 = list(Y)
common = set(list1) & set(list2)
common_num = []

for i in common:
    common_num = common_num + [i]*min(list1.count(i), list2.count(i))
#print(common_num)


if common_num == []:
    answer = "-1"
elif common_num[0] == "0":
    answer = "0"
else:
    answer = "".join(sorted(common_num, reverse=True))


print(answer)    


