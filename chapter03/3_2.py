'''
책의 방법
★반복되는 수열에 대해 파악

반복되는 수열의 길이 (k+1)
반복되는 횟수 == m / (k+1)
가장 큰 수가 등장하는 횟수 == (m / (k+1))*k
m / (k+1)이 나누어 떨어지지 않는 경우 
--> m % (k+1)만큼 가장 큰 수가 더해짐
따라서 가장 큰 수가 더해지는 횟수는 int(m/(k+1)*k+ m % (k+1))
'''
#n, m, k를 공백으로 구분해 입력받기
n, m, k = map(int, input().split())
#n개의 수를 공백으로 구분해 입력받기
num = list(map(int, input().split()))

num.sort() #정렬
maxi = num[n-1] #가장 큰 수
sec_maxi = num[n-2] #두 번째 큰 수

#가장 큰 수가 더해지는 횟수 계산
cnt = int(m / (k +1)) * k
cnt += m % (k+1) #나누어 떨어지지 않는 경우 나머지만큼 가장 큰 수를 추가 덧셈

result = 0
result += (cnt)* maxi #가장 큰 수 덧셈
result += (m-cnt) * sec_maxi #두 번째 큰 수 덧셈
