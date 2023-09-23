'''
큰 수의 법칙
n개의 수를 m번 더해(연속 k번) 가장 큰 수를 만듦

입력받기
수를 리스트 형태로 입력받아 정렬시킨 후 가장 큰 값과 두번재로 큰 값 추출
가장 큰 값을 연속 k번 더한 후 그 횟수가 소진될 경우 두번째로 큰 값을 더해주고 다시 k번 더함을 반복
'''
n, m, k = map(int, input().split())

num = list(map(int, input().split()))

num.sort() #정렬
maxi = num[n-1]
sec_maxi = num[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0: #더할 수 있는 횟수를 모두 소진한 경우
            break
        m -= 1
    if m == 0:
        break
    result += sec_maxi #두번째 큰 수 더하기
    m -= 1

print(result)
