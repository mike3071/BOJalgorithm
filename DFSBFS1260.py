from collections import deque
v, e, s = map(int, input().split())
graph = [[] for i in range(v+1)]
for j in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for i in range(v+1):
    graph[i].sort()
dfsvisited = [0]*(v+1)
bfsvisited = [0]*(v+1)
dfsresult=[]
bfsresult=[]
def dfs(k):
    dfsresult.append(k)
    dfsvisited[k]=1
    for q in graph[k]:
        if dfsvisited[q]==0:
            dfs(q)
def bfs(k):
    bfsresult.append(k)
    bfsvisited[k]=1
    queue = deque()
    queue.append(k)
    while queue:
        m = queue.popleft()
        for w in graph[m]:
            if bfsvisited[w]==0:
                queue.append(w)
                bfsresult.append(w)
                bfsvisited[w]=1
dfs(s)
bfs(s)
for i in dfsresult:
    print(i, end=' ')
print()
for i in bfsresult:
    print(i, end=' ')
