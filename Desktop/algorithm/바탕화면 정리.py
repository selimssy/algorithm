wallpaper = [".#...", "..#..", "...#."]

result = []

for i in range(len(wallpaper)):
    if "#" in wallpaper[i]: 
        result.append(i)
        break

result.append(min([s.index("#") for s in wallpaper])) 

for i in range(len(wallpaper)-1, -1, -1):
    if "#" in wallpaper[i]: 
        result.append(i)
        break
        
result.append(max([s.index("#") for s in wallpaper])) 

print(result)