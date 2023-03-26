beads = [100,500,500,900,950]
beads.sort()  # 구슬을 무게를 기준으로 오름차순으로 정렬

bins = []  # 빈 주머니 리스트를 만듦

for b in reversed(beads):
    best_bin = None
    for bin in bins:
        if sum(bin) + b <= 1000 and  (best_bin is None or sum(bin) > sum(best_bin)):
            best_bin = bin
    if best_bin is None:
        best_bin = []
        bins.append(best_bin)
    best_bin.append(b)

print(len(bins))  # 필요한 주머니 갯수 출력