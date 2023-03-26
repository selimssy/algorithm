n = 4
m = 1
section = [1, 2, 3, 4]
paint = []

for s in section:
    if paint and (s - paint[-1][0]) <= (m-1):
        paint[-1].append(s)
    else:
        paint.append([s])

print(paint)
print(len(paint))


print(sorted([4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
