'''
숫자 카드 게임
n*m 카드의 행마다 가장 낮은 카드를 추출할 수 있을 때
최종적으로 가장 큰 수를 뽑도록 유도

각 행마다 가장 작은 수를 찾아 그 중 가장 큰 수를 찾아냄
'''
n, m = map(int, input().split())

result = 0
for i in range(n):
    num = list(map(int, input().split()))
    mini = min(num) #최소값 찾기
    result = max(result, mini) #그 중 가장 큰 값

print(result)
