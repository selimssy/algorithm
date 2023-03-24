nums1 = [1,2]
nums2 = [10,20]
plus = list(map(lambda x,y: x+y, nums1, nums2))
#print(plus) # [11, 22, 33, 44, 55]
#if plus == [11, 22, 33, 44, 55]:
    #print("일치") # 일치




        


park = ["XXX","XSX","XXX"]
routes = ["N 1"]



obstruct = []
idx = -1
park_str = "".join(park)

H = len(park)
W = len(park[0])


x = park_str.index("S") % len(park[0])
y = park_str.index("S") // len(park[0])
position = [y,x]

for i in range(park_str.count("X")):
    obstruct.append([park_str.index("X", idx+1) // len(park[0]) , park_str.index("X", idx+1) % len(park[0])])
    idx = park_str.index("X", idx+1)
print(obstruct)   

def check_obstruct(n1, n2, n3, n4):
    return any([True for i in obstruct if min(n1,n2) <= i[1] <= max(n1,n2) and min(n3,n4) <= i[0] <= max(n3,n4)])  # 장애물 하나라도 걸리면 이동 못 함  

print([y,x])
for i in routes:         
        a = 0
        b = 0
        s = i[0]
        num = int(i[2])
        if s == "E":
            a += num
        elif s == "W":
            a -= num
        elif s == "S":
            b += num
        else:
            b -= num 

        if ((not 0 <= x+a <= (W-1)) or (not 0 <= y+b <= (H-1)) or check_obstruct(x, x+a, y, y+b)):
            print("이동 안 함")
            continue

        x +=a
        y += b    
        position = [y,x]
        print(position)      

#print(position)  