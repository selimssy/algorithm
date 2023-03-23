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




list1 = ["hello", "world", "try", "bye"]
sorted_list = sorted(list1, key=lambda x: x[-1])
print(sorted_list)

my_list = ["apple", "banana", "cherry"]
my_list.sort(key=len)
print(my_list)




# map() 함수 : map(함수, 적용할 요소1, 적용할 요소2...)
nums = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, nums)
print(list(squares))

nums1 = [1,2,3,4,5]
nums2 = [10,20,30,40,50]
plus = list(map(lambda x,y: x+y, nums1, nums2))
print(plus)




# filter 함수 : 입력한 함수의 반환값이 True인 항목으로 새로운 시퀀스를 반환
s = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, s)
print(list(even))

#filter함수 직후 타입
print(type(filter(lambda x: x%2==0, s)))  # <class 'filter'>



# 리스트 정렬 기준 여러개
str_list = ['cat', 'dog', 'tiger', 'rabbit', 'elephant']
str_list.sort(key=lambda x: (len(x), x[0]))
print(str_list)

list3 = ["cat", "cattt", "dog", "doggg", "tiger", "tigerrrr", "rabbit", "rabbitttt", "elephant", 'elephantttt']
list3.sort( key=lambda x: (x[0], -len(x)))  # 일단 첫글자로 오름차순, 첫 글자 같으면 글자수로 내림차순(-len(x))
print(list3)




# 리스트 특정 원소 반복: extented()
old_list = [1, 2, 3, 4, 5]
extend_list = []

while len(extend_list) <= 50: #원소 50개까지만
    extend_list.extend(old_list)
    
print(extend_list)



# 반복되는 패턴 함수 만들기
pattern_num = [2, 1, 2, 3, 2, 4, 2, 5]
def pattern(x):  # x번째 수(0부터)
    return pattern_num[x % len(pattern_num)]
print(pattern(7))


# 배열 출력 선언 없이
print([1,2,3][2])



def same(x):
    answers = [1,2,3,4,5]
    if [1,3,3,2,5][x % 5] == answers[x]:
        return True
    else:
        return False
print(same(1))    





# items()함수, 리스트 컴프리헨션 
dict1 = {"car": 7000, "bus": 1500, "subway": 1300}
print(dict1.items())
key1 = [key for key, value in dict1.items() if value == 1500]
print(key1)



# lambda 사용해서 딕셔너리 value로 key값 출력
dict2 = {"car": 7000, "bus": 1500, "subway": 1300}

key2 = list(filter(lambda x: dict2[x] == 1500, dict2))
print(key2)



# enumerate


#문자열 각각의 문자를 리스트로
str3 = "12345"
chars = list(str3)
print(chars)

#위를 숫자로
str3 = "12345"
nums3 = [int(str3[i]) for i in range(len(str3))]
print(nums3)




# if를 사용한 리스트 생성 (짝수만 걸러서 2배 곱하는 리스트)
test = [1,2,3,4,5]
res = [2* i for i in test if i % 2 == 0]
print(res) # [4, 8]



# index(), find() 함수 - 둘의 차이 : index는 없으면 에러 발생, find는 없으면 -1반환
s = "apple"
s.index("a")
s.find("k", -1)



# 문자열 뒤집기
str4 = "hello"
r_str = str4[::-1]
print(r_str)
