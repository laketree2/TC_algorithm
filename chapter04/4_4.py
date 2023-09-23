'''
게임 개발
- 맵 크기 입력받기
- 현재 위치(방문처리)와 방향 입력받기

# 구현(생각해야함)
- 왼쪽방향으로 돌 수 있는 블록(함수)
- 1단계를 무조건 실행해야하므로 재귀함수 형태
ㄴ방향은 4가지

- 다음 경로 판별할 수 있는 조건문 생성
ㄴ 육지라면 왼쪽방향으로 전진
ㄴ 네 방향 모두 가본 칸이러가 바다라면 방향 유지
한 후 한칸 뒤로 간 뒤 회귀
ㄴ 그 뒷 칸도 바다라면 멈춘 후 1단계 회귀

방문 확인하는 문제와 유사
좌표평면에서 배열과 배열 자체의 특성
arr[x][y] 좌표
arr[y:위치][x:요소]
'''
n, m = map(int, input().split()) #맵 크기 입력받기
x, y, d = map(int, input().split()) #현재 좌표와 방향 입력받기

arr = []
for i in range(n): #줄 단위로 받아서 저장
    arr.append(list(map(int, input().split())))

#어려웠던 부분
game_map = [[0] * m for _ in range(n)]
arr[x][y] = 1

dir = [0, 1, 2, 3] #북동남서
d = dir[dir.index(d) - 1]

#이동 가능한 좌표 설정
dx = [0, 1, 0, -1] 
dy = [1, 0, 1, 0]

#왼쪽으로 회전하는 함수(어려움)
# def turn_left():
#     global d #0123
#     d -= 1 #북동남서 --> 1씩 감소하면 왼쪽 방향
#     if d == -1: #음수가 될 경우 
#         d = 3 
    
temp = 1 #방문 칸 수 저장할 변수 초기화(현재 칸은 항상 방문상태이므로 1부터 시작)

for r in range(m):
    for c in range(n):
        i = 0
        while i < 4:
            nx = x + dx[d]
            ny = y + dy[d]
            if(arr[ny][nx] == 0): #왼쪽 방향에 0이 있으면
                d = dir[dir.index(d) - 1]
                x, y = nx, ny #왼쪽 한 칸 전진
                arr[x][y] = 1 #방문처리
                temp += 1 #카운팅
                i = 0
            else:
                d = dir[dir.index(d) - 1]
                i += 1

        # 한 칸 후진
        nx = x - dx[d]
        ny = y - dy[d]

        #후진 가능하면 1단계 회귀
        if arr[nx][ny] == 0:
            x, y = nx, ny
            arr[x][y] = 1 #방문처리
            temp += 1

        #모두 불가능하면 탈출
        else:
            break


print(temp)
