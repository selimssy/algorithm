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



# 딕셔너리에서 key만 추출
d1 = {"0":2, "1":1, "2":1, "3":1} 
print(d1.keys())  # dict_keys(['0', '1', '2', '3']) 
# 얘를 set() 함수를 써서 두 딕셔너리에서 공통으로 존재하는 key값 구하는 등으로 응용 가능




# 문자열에서 해당 문자가(여기선 숫자)가 몇 번씩 있는지 + 문자열에서 각각의 문자열을 for로 접근
string = "12234"
dict = {int(char): string.count(char) for char in string}
print(dict)
string2 = "가가가나다라"
print(string2.count("가"))
print([char for char in string])





# join함수  -- 기본 문법:  구분자.join(문자열 or 리스트 or 튜플 등)   
join_list = ['안', '녕', '하', '세', '요']
print("".join(join_list)) # 안녕하세요
print("_".join(join_list)) # 안_녕_하_세_요




# 0이 5번인 리스트 생성법
# 1. for 사용
list1 = [0 for _ in range(5)]
#2. ★★★리스트 덧셈 사용★★★ --------이걸 주로 써야
list2 = [0] * 5
print(list1) #[0, 0, 0, 0, 0]
print(list2) #[0, 0, 0, 0, 0]
print(list1 + list2) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

common_num = [0]
print(common_num + [1]*2)





# 문자열 각각의 문자를 리스트로 생성하는 간단한 방법
s = "5525"
print(list(s))




 
# 특정 원소가 리스트에 몇 개 있는지 출력
list1 = [10,20,20,30,30,30,40,40,40,40,50,50,50,50,50]
print(list1.count(30)) #3
print(list1.count(50)) #5




# 문자열 리스트에서 부분적으로 포함되는 요소 추출
list2 = ['hello', 'helloJenny', 'hi']
new = [str for str in list2 if 'hello' in str]
print(new)



# 리스트 컴프리헨션에서 lambda 사용하는 예제
squares = [(lambda x: x**2)(x) for x in range(10) if x%2 == 0]
print(squares)  # [0, 4, 16, 36, 64]



original_list = ['apple', 'banana', 'cherry']
reversed_list = list(map(lambda x: ''.join(reversed(x)), original_list))
print(reversed_list)  # ['elppa', 'ananab', 'yrrehc']


str = "abcabcabc"
print(list(reversed(str)))





# 
str1 = "?????ABC"
s1 = "ABCqq"
s2 = "qqABC"
print(str1.count("?"))  # 5
print(str1.index("ABC")) # 5

print(s1.find(str1.replace("?",""))) #0
print(s2.find(str1.replace("?",""))) #2

# x.index(i.replace("?","")) == i.count("?") or x.index(i.replace("?","")) == 0


list1 = [1,2,3,4,5]
print(list1[(5+1)%2])




list1 = [10,20,30,40,50]
print(max(list1[0:3]))  # 30
print(sorted(list1[0:3], reverse=True)[3-1]) 


nums1 = [1,2,3,4,5]
nums2 = [10,20,30,40,50]
plus = list(map(lambda x,y: x+y, nums1, nums2))
print(plus) # [11, 22, 33, 44, 55]
if plus == [11, 22, 33, 44, 55]:
    print("일치") # 일치

print("".join(["SOO","OXX","OOO"]).count("X"))  #2 




# 알아둬야 할 True, False 연산법
print(not 3 <= 5 <= 6)  




# any() 함수는 인자로 받은 iterable 객체(리스트, 튜플, 집합 등) 중에서 하나라도 True인 값이 있으면 True를 반환하고, 
# 모두 False인 경우에만 False를 반환



## n의 약수 갯수 구하는 방법 2가지 중에서

# 1.리스트 컴프리헨션 이용하고 len으로 갯수 구하는거랑
list1 = [i for i in range(1,17) if 16 % i == 0]
print(len(list1))

# 2. 변수 사용하는 것 중에서 이게 더 효율적
def divisors(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


# 그리고 제곱근까지만 for 돌리는 이게 더 효율적
import math
def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            count += 2
            if i == n // i:
                count -= 1
    return count



# 바꾸려는 문자 없어도 에러 안뜬다!
print("abc".replace("d", ""))



# 
str = "a5"
print(str[0].isdigit()) #False
print(str[1].isdigit()) #True




## 다음은 파이썬 리스트 컴프리헨션과 lambda 함수를 사용하여 ['abc', 'ab', 'efg']의 원소 길이가
#  짝수이면 원소의 첫 번째 글자를, 홀수이면 두 번째 글자를 추출하여 리스트로 반환하는 예제 
words = ['abc', 'ab', 'efg']
result = [(lambda x: x[0] if len(x)%2 == 0 else x[1])(word) for word in words]
print(result) #['b', 'a', 'f']




# 딕셔너리 in으로 있는지 확인하기
index = {'TR':0, 'FC':0, 'MJ':0, 'NA':0}
print('TR' in index)  # True



# 딕셔너리 key, value 사용한 딕셔너리 컴프리헨션
fruits = {'car': 1, 'bus': 2, 'train': 3, 'subway': 4}
items = [(key, value) for key, value in fruits.items()]
values = list(fruits.values())
keys = list(fruits.keys())
print(items)  # [('car', 1), ('bus', 2), ('train', 3), ('subway', 4)]
print(values) # [1, 2, 3, 4]
print(keys) # ['car', 'bus', 'train', 'subway']





# replace 횟수 제한하려면 3번째 인자로 횟수 쓰면 된다!!





# 파이썬 숫자로 이루어진 리스트 [1,2,3,4,5]를 문자열 "12345"로 만드는법(join함수 쓰는게 for문 써서 += 작업하는 것보다 빠르다!!★)
'''
numbers = [1, 2, 3, 4, 5]
numbers_str = ''.join(map(str, numbers))
print(numbers_str)  # "12345"
'''



## 날짜 관련 함수
from datetime import datetime

def date(date):
    return datetime.strptime(date, '%Y.%m.%d')

print(date("2021.05.02")) #2021-05-02 00:00:00


# "2021.05.02" 에 해당하는 날짜에 n개월 더하는 방법
date_string = "2021.05.02"
date = datetime.strptime(date_string, "%Y.%m.%d")
n = 6
new_date = date.replace(month=date.month + n)

print(new_date.strftime("%Y.%m.%d"))

# "2021.05.02" 에 해당하는 날짜에 n일 빼는 방법
import datetime
date_str = "2021.05.02"
date_obj = datetime.datetime.strptime(date_str, "%Y.%m.%d")

new_date_obj = date_obj - datetime.timedelta(days=1)

# strftime :d atetime 객체를 지정된 형식의 문자열로 변환하는 메서드
new_date_str = new_date_obj.strftime("%Y.%m.%d")
print(new_date_str) # 2021.04.25





terms = ["A 6", "B 12", "C 3"]
each_term = {term[0]:int(term[2:]) for term in terms}
print(each_term)





from datetime import datetime, timedelta

input_date = datetime.strptime('2022-05-19', '%Y-%m-%d')

new_month = input_date.month + 11
new_year = input_date.year

if new_month > 12:
    new_month -= 12
    new_year += 1

output_date = input_date.replace(year=new_year, month=new_month)

print(output_date.strftime('%Y-%m-%d'))







string = "3 - 4 = -3"
expression = string.split('=')[0].strip()
value = string.split('=')[1].strip()

quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
print(["O" if eval(str.split('=')[0].strip()) == int(str.split('=')[1].strip()) else "X" for str in quiz])

list1 = []
list2 = [1]
if list1:
    print("111")
if list2:
    print("222")    # 얘만 출력(비어있지 않을 때만 출력)


print(sorted([10, 30, 80, 20, 50, 70, 40, 40, 90]))




beads = [10, 30, 80, 20, 50, 70, 40, 40, 90]
beads.sort()  # 구슬 무게를 기준으로 정렬
bins = []  # 주머니 리스트
for b in beads:
    # 현재 주머니가 존재하고, 주머니의 무게와 구슬의 무게를 더한 값이 100 이하일 때
    if bins and (sum(bins[-1]) + b) <= 100:
        # 현재 주머니에 구슬 추가
        bins[-1].append(b)
    else:
        # 새로운 주머니 생성하여 구슬 추가
        bins.append([b])
print(len(bins))  # 필요한 주머니 개수 출력





# for i in range(9,-1,-1) :   이게뭐지