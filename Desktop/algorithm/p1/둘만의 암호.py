s = "ybcde"
skip = "az"
index = 1

#a = [chr(ord(char)+  index + len(list(filter(lambda x: x in skip,  [alpha(char,i) for i in range(1,index+1)]   )    )))  for char in s]
answer = ""
alpha = [chr(i) for i in range(97, 123)]
element = list(filter(lambda x: x not in list(skip), alpha)) # 순환 대상 알파벳
print("".join([element[(element.index(char) + index) % len(element)] for char in s]) )



'''
def res_alpha(s,n):
    element = list(filter(lambda x: x not in list(skip), alpha)) # 순환 대상 알파벳
    return element[(element.index(s) + n) % len(element)]
'''
'''
def res_alpha():
    element = list(filter(lambda x: x not in list(skip), alpha)) # 순환 대상 알파벳
    return "".join([element[(element.index(char) + index) % len(element)] for char in s])  
'''

#a = [res_alpha(char, index + len(set(list(filter(lambda x: x in skip, [res_alpha(char,i) for i in range(1,index+1)]))))) for char in s]
#print(a)
#print(res_alpha(s,index))

'''
for char in s:
    num = index 
    
    while(True):
        if res_alpha(char,num) not in skip:
            break
        num +=1
    answer += res_alpha(char,num)
print(answer)
'''

'''
for char in s:
    answer += res_alpha(char,index)
print(answer)    

print("".join([res_alpha(char,index) for char in s])) 
'''

#print(res_alpha())