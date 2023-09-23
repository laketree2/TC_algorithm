'''
계수정렬
'''
n = int(input())
n_list = [0]*1000001

#가게 전체 부품 번호 기록
for i in input().split():
    n_list[int(i)] = 1

#손님 부품 개수 입력받기
m = int(input())
m_list = list(map(int, input().split()))

for i in n_list:
    if n_list[i] == 1:
        print('yes', end= " ")
    else:
        print('no', end= " ")