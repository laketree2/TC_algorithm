#피보나치 함수 재귀 함수 구현
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))
#수행 시간이 기하급수적으로 늘어남 = 시간초과 우려(O(2**n)) 