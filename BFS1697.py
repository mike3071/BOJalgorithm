'''
틀렸다는데 왜 틀렸는지 알 수가 없음... 직관적으로 감은 오는데 명백하게 설명이 불가
from collections import deque
N, K = map(int, input().split())
check = [0] * 100001
def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            return check[K]
        if v <= 50000 and check[v*2]==0:
            q.append(v*2)
            check[v*2]=check[v]+1
        if v < 100000 and check[v+1]==0:
            q.append(v+1)
            check[v+1]=check[v]+1
        if v > 0 and check[v-1]==0:
            q.append(v-1)
            check[v-1]=check[v]+1
print(bfs())
'''

from collections import deque
N, K = map(int, input().split())
check = [0] * 100001
def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            return check[K]
        if v > 0 and check[v-1]==0:
            check[v-1]=check[v]+1
            q.append(v-1)
        if v < 100000 and check[v+1]==0:
            check[v+1]=check[v]+1
            q.append(v+1)
        if v <= 50000 and check[v*2]==0:
            check[v*2]=check[v]+1
            q.append(v*2)
print(bfs())
