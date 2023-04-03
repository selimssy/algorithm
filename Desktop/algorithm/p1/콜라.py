a=3
b=2
n=10
answer = 0

while(n >= a):
    answer += n//a * b
    n = n//a * b + n % a

print(answer)    