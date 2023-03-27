from collections import Counter
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


participant = dict(Counter(participant))
completion = dict(Counter(completion))

for key, value in participant.items():
    try:        
        if value != completion[key]:
            print(key)
    except:
        print(key)        



dict1 = Counter([1,1,1,1,2,2,2,3,3])
dict2 = Counter([1,1,1,1])
# Counter끼리 먼저 빼고 나중에 dict()
print(dict(dict1 - dict2))  # {2: 3, 3: 2}      