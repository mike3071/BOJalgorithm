'''
시간 초과, 메모리 초과
from collections import deque
import copy
m, n = map(int, input().split())
maplist=[]
mapslist=[maplist]
for i in range(m):
    yolo = input()
    appendyong=[]
    for c in yolo:
        c = int(c)
        appendyong.append(c)
    maplist.append(appendyong)
for j in range(m):
    for k in range(n):
        if j>=1 and j<(m-1):
            if maplist[j][k]==1 and maplist[j+1][k]==0 and maplist[j-1][k]==0:
                copymap = copy.deepcopy(maplist)
                copymap[j][k] = 0
                mapslist.append(copymap)
        if k>=1 and k<(n-1):
            if maplist[j][k]==1 and maplist[j][k+1]==0 and maplist[j][k-1]==0:
                copymap = copy.deepcopy(maplist)
                copymap[j][k] = 0
                mapslist.append(copymap)
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
def bfs(x, y, k):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for l in range(4):
            nx=x+dx[l]
            ny=y+dy[l]
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if k[nx][ny]==1:
                continue
            if k[nx][ny]==0:
                queue.append((nx, ny))
                k[nx][ny] = k[x][y] + 1
    if k[m-1][n-1]==0:
        return 1000001
    return k[m-1][n-1]
a = 1000001
for b in mapslist:
    a=min(a, bfs(0, 0, b))
if a == 1000001:
    print(-1)
else:
    print(a+1)
'''
