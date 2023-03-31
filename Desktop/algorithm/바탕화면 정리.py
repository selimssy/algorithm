wallpaper = ["#"]

result = []

for i in range(len(wallpaper)):
    if "#" in wallpaper[i]: 
        result.append(i)
        break
   

result.append(min([s.index("#") for s in wallpaper if "#" in s])) 

for i in range(len(wallpaper)-1, -1, -1):
    if "#" in wallpaper[i]: 
        result.append(i+1)
        break
      
result.append(max([s.rindex("#") for s in wallpaper if "#" in s]) + 1) 

print(result)