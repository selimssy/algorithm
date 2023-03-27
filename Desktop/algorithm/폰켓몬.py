nums = [3,3,3,2,2,2]



n = int(len(nums) * 0.5)
num = set(nums)
나머지 = set(nums).difference(num)

if len(num) >= n:
    print(n)
else: 
    print(len(num))