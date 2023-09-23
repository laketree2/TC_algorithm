'''
떡볶이 떡 만들기
이진탐색
★잘랐을 때 떡의 양과 목표값 비교
'''
#백준 2805
import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
array = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    ricecake = 0
    mid = (start + end) // 2 #중간값 계산
    # ★어려웠던 부분
    # 잘랐을 때 떡 길이 계산
    for i in array:
        if i > mid:
            ricecake += i - mid
    #떡 양이 부족한 경우 왼쪽 탐색
    if ricecake < m:
        end = mid - 1
    #충분한 경우 오른쪽 탐색
    else:
        result = mid #중간점 처리
        start = mid + 1 #이전단계에서 중간점 처리 -> 단계 늘리기
    
print(result)

