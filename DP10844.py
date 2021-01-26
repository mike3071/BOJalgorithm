n = int(input())
dp = list(([1]*10 for _ in range(n)))
if n!=1:
    for i in range(1,n):
        for j in range(10):
            if j == 0:
                dp[i][0] = dp[i-1][1]
            elif j == 9:
                dp[i][9] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1]+ dp[i-1][j+1]
print(sum(dp[n-1][1:])%1000000000)
