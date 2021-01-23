anum = int(input())
alist = list(map(int, input().split()))
alist.sort()
checknum = int(input())
checklist = list(map(int, input().split()))

def binary(k):
    start = 0
    end = anum-1
    while start<=end:
        mid = (start+end)//2
        if alist[mid] == k:
            return 1
        elif alist[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in checklist:
    print(binary(i))
