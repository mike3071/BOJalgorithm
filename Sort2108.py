import sys
num = int(sys.stdin.readline())
listing = []
rare = {}
for i in range(num):
    value = int(sys.stdin.readline())
    listing.append(value)
    if value not in rare:
        rare[value]=1
    else:
        rare[value]+=1
listing.sort()
if (sum(listing)/len(listing))-((sum(listing)/len(listing))//1) >=0.5:
    mean = int(((sum(listing)/len(listing))//1)+1)
else:
    mean = int(((sum(listing)/len(listing))//1))
mid = listing[(len(listing)//2)]
k = list(rare.values())
q = max(k)
w = []
for i in list(rare.keys()):
    if rare[i] == q:
        w.append(i)
w.sort()
if len(w) != 1:
    most = w[1]
else:
    most = w[0]
ranging = listing[-1]-listing[0]
print(mean)
print(mid)
print(most)
print(ranging)
