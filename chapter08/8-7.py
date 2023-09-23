#백준 11726 11727
import sys
input = sys.stdin.readline
print = sys.stdout.write

dp = [0]*1001

dp[1] = 1
dp[2] = 3

n = int(input())
for i in range(3, n+1):
    dp[i] = (dp[i-1]+dp[i-2]*2)%796796
print(str(dp[n]))


