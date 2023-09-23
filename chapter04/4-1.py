n = int(input()) #n 입력받기
plan = input().split() # 이동 계획 입력받기
LRUD = ['L', 'R', 'U', 'D'] #상하좌우 이동값(왼0, 오1, 위2, 아래3)

# 현재 위치 변수 초기화
ax, ay = 1, 1

# 이동 좌표 변수 초기화
# nx, ny = 0, 0

dx = [0, 0, -1, 1] # 이동할 수 있는 x좌표
dy = [-1, 1, 0, 0] # 이동할 수 있는 y좌표

#어려웠던 부분
for p in plan: # 전체를 순회하면서 이동 검사
    for i in range(4): # 방향은 총 4개
        if p == LRUD[i]: # ★이동하려는 값과 인덱스 번호 매칭
            nx = ax + dx[i]
            ny = ay + dy[i]
    #공간 이탈시 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    #이동된 현재 값 저장
    ax, ay = nx, ny
print(ax, ay)
