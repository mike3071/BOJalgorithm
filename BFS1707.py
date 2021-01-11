from collections import deque
import sys
input = sys.stdin.readline
def bfs(k):
    color[k]=1
    queue = deque()
    queue.append(k)
    while queue:
        out=queue.popleft()
        for i in graphshape[out]:
            if color[i]==0:
                color[i]= (- color[out])
                queue.append(i)
            else:
                if color[i]==color[out]:
                    return 'NO'
    return 'YES'
  
    
    
num = int(input())
for i in range(num):
    v, e= map(int,input().split())
    graphshape = [[] for _ in range(v+1)]
    color = [0]*(v+1)
    for j in range(e):
        start, end = map(int, input().split())
        graphshape[start].append(end)
        graphshape[end].append(start)
    ans = 'YES'
    for r in range(1,v+1):
        if color[r]==0:
            p = bfs(r)
            if p == 'NO':    
                ans = 'NO'
                break
    print(ans)
    
