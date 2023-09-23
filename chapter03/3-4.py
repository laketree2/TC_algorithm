'''
1이 될 떄까지
어떤 수 n이 1이 될 떄 까지 n에서 1을 빼거나 n을 k로 나눌 수 있음(나누어 떨어질 때)
과정반복 최소값

최대한 많이 나누어야 함, 나누어지지 않을 때 1빼기
n이 k보다 크면 나눌 수 있음
n이 k로 나누어 떨어지면 나눌 수 있음
나누어떨어지지 않을 때 1 빼기
횟수 1 추가
'''
n, k = map(int, input().split())
result = 0

while n >=k:
    while n % k !=0: #0이 아니면 
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
