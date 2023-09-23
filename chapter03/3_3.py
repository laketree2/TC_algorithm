#책의 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    num = list(map(int, input().split()))
    mini = 10001 #현재 줄에서 가장 작은 수 찾기
    for a in num:
        mini = min(mini, a)
    result = max(result, mini)

print(result)
