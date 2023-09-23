#백준 14503
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

# 어려웠던 부분
d = [[0] * m for _ in range(n)] #0으로 채워진 배열 공간 만들기
#print(d) 확인용
x, y, direction = map(int, sys.stdin.readline().rstrip().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 맵 정보를 입력받아 생성된 배열 공간에 집어넣기
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split()))) 
#print(array) 확인용

#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0

print(count)
