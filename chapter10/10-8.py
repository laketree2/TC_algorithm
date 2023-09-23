#도시 분할 계획
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x: #예상한 부모 값이 아닐 때(union이 한 번 이루어 졌을 때)
        parent[x] = find_parent(parent, parent[x]) #부모 찾기 
    return parent[x]

def union_parent(parent, a, b): #제일 작은 부모 노드 통합
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
v, e = map(int, input().split())
parent = [i for i in range(v+1)] #인덱스 1부터 시작, 1 무시
info = list()
for _ in range(e):
    a, b, c = map(int, input().split())
    info.append((c, a, b)) #가중치를 먼저 내세워 
info.sort() #★가중치 기준으로 정렬(가중치 작은 순)

total = [] #가중치
for i in range(e):
    c, a, b = info[i]
    # 사이클이 발생하지 않는 경우에만 집합에 포함(연결)
    if find_parent(parent, a) != find_parent(parent, b): #부모 노드가 다르면
        union_parent(parent, a, b) #부모 통합
        total.append(c) #가중치 추가
total.pop()
print(sum(total))