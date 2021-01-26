count = int(input())
for _ in range(count):
    n = int(input())
    onelist = [0]*(n+1)
    zerolist = [0]*(n+1)
    if n >=1:
        onelist[1] = 1
    zerolist[0] = 1
    if n >= 2:
        for i in range(2, n+1):
            onelist[i] = onelist[i-1] + onelist[i-2]
            zerolist[i] = zerolist[i-1] + zerolist[i-2]
    print(zerolist[n], onelist[n])
