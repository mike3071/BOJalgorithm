import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    q = int(input())
    m.append(q)

m.sort()

for i in m:
    print(i)
    
import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    q = int(input())
    m.append(q)

m.sort()

for i in m:
    print(i)
    
# 선택정렬
import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    q = int(input())
    m.append(q)

for i in range(n):
    index = i
    for j in range(i+1,n):
        if m[index]>m[j]:
            index = j
    m[index], m[i] = m[i], m[index]

for i in m:
    print(i)
# 삽입정렬
import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    q = int(input())
    m.append(q)

for i in range(1, n):
    for j in range(i, 0, -1):
        if m[j]<m[j-1]:
            m[j], m[j-1] = m[j-1], m[j]
        else:
            break

for i in m:
  print(i)
#계수정렬
import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    q = int(input())
    m.append(q)
l = [0]* (max(m)+1)
for i in m:
    l[i] +=1

for i in range(max(m)+1):
    for j in range(l[i]):
        print(i)
# 퀵정렬
import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    q = int(input())
    m.append(q)

def quick (start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and m[left] <= m[pivot]:
            left +=1
        while right > start and m[right] >= m[pivot]:
            right-=1
        if left <= right:
            m[left], m[right] = m[right], m[left]
        else:
            m[right], m[pivot] = m[pivot], m[right]
    quick (start, right-1)
    quick (right+1, end)
quick(0, len(m)-1)
            
for i in m:
    print(i)
