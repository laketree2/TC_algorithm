'''
상하좌우
- 공간 크기 n 입력받기(int)
- 이동 계획 plan 입력받기(입력받은 문자열 나누기)
- ★이동할 수 있는 좌표의 경우의 수와 상하좌우 문자열 매칭시키기
ㄴ 리스트 인덱스 번호로 매칭
ㄴ 딕셔너리 매칭?
- for반복문을 통해 입력받은 plan이 끝날 때 까지 반복
- if: 범위를 이탈할 경우 --> 입력 무시
- 이동된 현재 위치를 각 좌표에 대입한 후 다음 입력 처리
- 최종 좌표 출력
'''

n = int(input()) #범위 입력받기
plan = input().split() #이동 계획 입력받기

#현재 좌표
ax, ay = 1, 1

#이동 가능한 좌표 처리
move = [(0,-1), (0, 1), (-1, 0), (1, 0)]
LRUD = ['L', 'R', 'U', 'D']

for i in plan:
    nx = ax + move[LRUD.index(i)][0]
    ny = ay + move[LRUD.index(i)][1]

    #범위 이탈시 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    #이동된 현재 값 저장
    ax, ay = nx, ny
print(ax, ay)
