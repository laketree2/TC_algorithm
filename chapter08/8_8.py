#책의 코드, 효율적인 화폐 구성

#정수 n, m 입력받기
n, m = map(int, input().split())

#n개의 화폐 단위 정보를 입력받기
arr = []
for i in range(n):
    arr.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [1001] * (m + 1)

#dp 보텀업 방식 진행
d[0] = 0
for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[j]] != 10001: #(i - k)를 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - arr[i]] + 1)

#계산된 결과 출력
if d[m] == 10001: #최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])