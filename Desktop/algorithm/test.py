print('*' * 3 + '\n' + 'aaa')


arr = []

for i in range(4):
    arr.append([]) # 새로운 내부 배열 선언
    for j in range(3):
        arr[i].append(0) # 해당 내부 배열에 0이라는 값 추가
arr[0][0] = 100
print(arr)        



# replace 할 때 기존 문자열을 바꿔줘야
str = '12345'
str = str.replace('1', '*')
print(str)


# 문자열 일부만 대문자로 바꾸는법
str = "hello"
str = str[0].upper() + str[1:]
print(str)



# ord, chr
print(ord('a')) #97
print(ord('1')) #49 
print(ord('0')) #48

print(chr(97)) #a
print(chr(49)) #1


# 문자 부등호
str = 'A'
if str >= 'A' and str <= 'Z':
    print("대문자")
elif str >= 'a' and str <= 'z':
    print("소문자")



# return s.isdigit() and len(s) in [4,6] 와...
# try except도 좋다ㅠ