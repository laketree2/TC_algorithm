#플로이드워셜, 플로이드(O(n^3))
#백준 11404
n, m = map(int, input().split())
G = [[float('inf')] * (n+1) for _ in range(n+1)] #입력시 적용이 안됨

#자기자신에서 자기자신으로 가는 비용 0 초기화
for i in range(n+1):
    G[i][i] = 0 #자기 자신


for _ in range(m):
    a, b = map(int, input().split())
    G[a][b] = min(G[a][b])#a에서 b가는 가중치값

#거쳐 갈 노드와 최종 목적지 입력받기
x, k = map(int, input().split())

#3중 반복문
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(1, n+1):
    #그래프 값을 순회하면서
    for i in range(1, n+1):
        if G[i][j] == float('inf'):
            G[i][j] = 0 #갈 수 없으면 0출력(문제조건)

distance = G[1][k] + G[k][x]

if distance >= float("inf"):
    print("-1")
else:
    print(distance)