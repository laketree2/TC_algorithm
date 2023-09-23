'''
학생 정보를 입력받아 낮은 순서대로 이름 출력
'''

n = int(input())

arr = []
for i in range(n):
    student = input().split()
    arr.append((student[0], int(student[1])))

#어려웠던 부분
arr = sorted(arr, key = lambda info: info[1])

for info in arr:
    print(info[0], end = " ")