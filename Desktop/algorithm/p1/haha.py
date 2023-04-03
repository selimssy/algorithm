words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
# [3, 2, 4, 1, 0]
res = []

for i in queries:
    print(list(filter(lambda x: len(x) == len(i) and (x.find(i.replace("?","")) == i.count("?") or x.find(i.replace("?","")) == 0), words)))
    res.append(len(list(filter(lambda x: len(x) == len(i) and (x.find(i.replace("?","")) == 0 or x[i.count("?"): ]== i.replace("?","")), words)))) 
print(res)

#res = [words.count(i) for i in queries]
#map(lambda str, words: words.count(len(str) == words[j] and str.replace("?","") in words[j]) , queries)



#print(res)            
