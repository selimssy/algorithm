strings = ["sun", "bed", "car"]
n = 1

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))