#퀵 정렬
#피벗을 기준으로 왼쪽은 작은, 오른쪽은 큰 인덱스 정렬 후 그들끼리 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗 첫 번째 원소
    left = start + 1
    left = end
    right = end
    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >=array[pivot]:
            right -= 1
        if left > right: #엇갈린 경우 작은 데이터와 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

        #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right-1)
        quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)
        