'''
수열 내림차순 정렬
'''

#첫째줄에 수열에 속해 있는 수의 개수 입력받기
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

#내림차순 정렬
arr = sorted(arr, reverse=True)

for i in arr:
    print(i, end=" ")
