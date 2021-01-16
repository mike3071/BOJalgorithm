v = int(input())
e = int(input())
graphshape = [[] for _ in range(v+1)]
visited = [1]
for k in range(v):
    visited.append(0)
for j in range(e):
    start, end = map(int, input().split())
    graphshape[start].append(end)
    graphshape[end].append(start)
def dfs(k):
    visited[k]=1
    for i in graphshape[k]:
        if visited[i]==0:
            dfs(i)
dfs(1)
cnt=0
for i in range(v+1):
    if visited[i]==0:
        cnt+=1
print(v-cnt-1)
