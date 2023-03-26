numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
result = ""

left = [1,4,7]
right = [3,6,9]

l = 0  # 왼손 숫자
r = 0  # 오른손 숫자

def pos(x):
    if 1<=x<=9:
        return (x-1)//3
    else:
        return 3


for num in numbers:
    if num in left:
        h = "L"
        l = num
    elif num in right:
        h = "R"
        r = num
    else:
        l_length = abs(pos(l) - pos(num))      
        r_length = abs(pos(r) - pos(num))  
        
        if l_length < r_length:
            h = "L"
            l = num
        elif l_length > r_length:
            h = "R"
            r = num
        else:
            h = hand.upper()[0]
            hand[0] = num                 

    result +=h


print(result)          