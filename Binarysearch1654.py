N, K = map(int,input().split())
lengthlist=[]
for _ in range(N):
    lengthlist.append(int(input()))
start = 0
end = max(lengthlist)
num = 0
length = 0
while start <= end:
    mid = (start+end)//2
    if mid == 0:
        mid = 1
    for i in lengthlist:
        num += i//mid
    if num >= K:
        length = mid
        start = mid + 1
    else:
        end = mid - 1
    num = 0
print(length)
