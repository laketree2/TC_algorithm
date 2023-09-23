'''
1로 만들기
백준 1463 
★어려웠던 부분 = dp 테이블 초기화(생소함)
상하좌우의 메모제이션 활용에 익숙해져야함
'''
n = int(input()) # 입력값 정수로 받기

#최소 계산수를 저장하기 위해 n+1개의 배열 선언
count = [n+1]*(n+1) 
count[1]=0 #숫자1은 자기자신이므로 0으로 초기화, 계산 줄이기

for i in range(2,n+1): #반복문
    tmp = [count[i-1]] #1을 뺀 경우
    if i%5==0: #5로 나눈 경우
        tmp.append(count[i//5]) #추가
    if i%3==0: #3으로 나눈 경우
        tmp.append(count[i//3]) #추가
    if i%2 == 0: #2로 나눈 경우
        tmp.append(count[i//2]) #추가
    count[i] = min(tmp)+1 #3가지 경우에서 최소값을 구해 1을 더함
    
print(count[n]) #출력