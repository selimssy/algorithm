survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]



index = {'TR':0, 'FC':0, 'MJ':0, 'NA':0}

for i in range(len(survey)):
    if survey[i] in index:        
        index[survey[i]] += (choices[i] -4)
    else: 
        index[survey[i][::-1]] += (choices[i] -4)*(-1)
    
print("".join([(lambda x,y: x[0] if y <0 else x[1])(key, value) for key, value in index.items()]))      #음수면 [0] [0] (<0)   양수면, 0이면(>=0) [1]

