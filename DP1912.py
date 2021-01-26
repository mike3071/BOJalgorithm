n = int(input())
origin = list(map(int, input().split()))
count = [0]*n
for i in range(n):
    if i == 0:
        count[i] = origin[i]
    else:
        count[i] = max((count[i-1] + origin[i]), origin[i])
print(max(count))
