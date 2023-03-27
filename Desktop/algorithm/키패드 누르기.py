numbers = [1,5]
hand = "right"
result = ""

left = [1,4,7,"*"]
right = [3,6,9,"#"]

'''
l = 0  # 왼손 숫자
r = 0  # 오른손 숫자 '''
pos = {"l":"*", "r":"#"}

def len_y(x):
    if x in ['*','#',0]:
        return 3
    else:
        return (x-1)//3
    '''
    if 1<=x<=9:
        return (x-1)//3
    else:
        return 3
    '''
def len_x(x):
    if x in left or x == "*":
        return 1
    elif x in right or x =="#":
        return 3
    else:
        return 2



for i in numbers:
    if i in left:
        h = "L"
        pos["l"] = i
    elif i in right:
        h = "R"
        pos["r"] = i
    else:
        l_length = (abs(len_x(pos["l"]) - len_x(i))) + (abs(len_y(pos["l"]) - len_y(i)))   
        r_length = (abs(len_x(pos["r"]) - len_x(i))) + (abs(len_y(pos["r"]) - len_y(i)))
        if l_length < r_length:
            h = "L"
            pos["l"] = i
        elif l_length > r_length:
            h = "R"
            pos["r"] = i
        else:
            h = hand.upper()[0]
            pos[hand[0]] = i

    result +=h
print(result)          




print(result == "LL")