'''
from collections import deque
def bfs(k):
    queue = deque()
    queue.append(k)
    color[k]=1
    while queue:
        out=queue.popleft()
        for i in graphshape[out]:
            if visited[i]==0 and color[out]==1:
                queue.append(i)
                color[i]=-1
                visited[i]=1
            if visited[i]==0 and color[out]==-1:
                queue.append(i)
                color[i]=1
                visited[i]=1
    for w in range(1,v+1):
        for q in graphshape[w]:
            if color[w]==color[q]:
                return 1
    return 0
    
    
num = int(input())
for i in range(num):
    v, e= map(int,input().split())
    graphshape = [[] for _ in range(v+1)]
    visited = [0]*(v+1)
    color = [0]*(v+1)
    for j in range(e):
        start, end = map(int, input().split())
        graphshape[start].append(end)
        graphshape[end].append(start)
    ans = 0
    for k in range(1, v+1):
        if color[k]==0:
            ans = bfs(k)
            if ans == 1:
                break
    if ans ==0:
        print('YES')
    else:
        print('NO')
'''
