babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

count = 0
babble = [ "aya", "ye", "woo", "ma" ]
for word in babbling:
    for text in babble:
        if text * 2 not in word:
            word = word.replace(text, ' ')   # 여기서 각각의 발음을 한 덩어리로 보기 위해서 " " 으로 바꿔야!!★ 
    if word.strip() == '':
        count += 1
