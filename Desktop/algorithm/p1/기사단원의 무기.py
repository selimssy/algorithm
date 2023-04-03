number = 10
limit = 3
power = 2



answer = 0

import math
def divisors(n):
    num = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            num += 2
            if i == n // i:
                num -= 1
    return num


for i in range(1, number+1):
    cnt = divisors(i)
    if cnt > limit:
        answer += power
    else:
        answer += cnt

print(answer)
