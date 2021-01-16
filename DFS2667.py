n = int(input())
graph=[]
for i in range(n):
    graph.append(list([]))
    k=input()
    for j in k:
        graph[i].append(int(j))
class dfs:
    def __init__(self):
        self.cnt=0
    def dfss(self, x, y):
        if 0<=x and x<n and 0<=y and y<n and graph[x][y]==1:
            self.cnt+=1
            graph[x][y]=2
            self.dfss(x-1, y)
            self.dfss(x, y-1)
            self.dfss(x+1, y)
            self.dfss(x, y+1)
total=[]
for q in range(n):
    for w in range(n):
        letsgo=dfs()
        letsgo.dfss(q, w)
        total.append(letsgo.cnt)
total.sort()
plus=0
realtotal=[]
for i in total:
    if i!=0:
        plus+=1
        realtotal.append(i)
print(plus)
for i in realtotal:
    print(i)
