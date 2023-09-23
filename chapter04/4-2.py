'''
시각(백준 18312)
1. 시각 입력받기
2. 시/분/초 나누어 3중 반복문 돌리기
3. 3이 포함된 경우 count++
'''

clock = int(input()) #시각 입력받기

count = 0 #3이 들어가는 시각의 개수를 입력받을 변수 초기화

for i in range(clock+1): #시분초 나누어 3중반복문
    for j in range(60):
        for m in range(60):
            if '3' in str(i) + str(j) + str(m): #3이 포함된 경우
                count += 1
print(count)
