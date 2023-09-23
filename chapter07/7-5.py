'''
n개 부품
m개 부품 확인
요청한 부품 번호의 순서대로 부품 확인
이진탐색
'''
def binary_search(n_list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        #찾은 경우 중간점 인덱스 반환
        if n_list[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif n_list[mid] > target:
            end = mid + 1
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int,input().split()))

#부품 확인
for i in m_list:
    result = binary_search(n_list, i, 0, n - 1)
    if result != None:
        print('yes', end= " ")
    else:
        print('no', end= " ")