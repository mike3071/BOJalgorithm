#pypy3에서 구동
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
lengthlist=list(map(int, input().split()))
start = 0
end = max(lengthlist)

result = 0
while start<=end:
    total = 0
    mid = ((start+end)//2)
    for i in lengthlist:
        if i > mid:
            total += i - mid
    if total >= K:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)   
