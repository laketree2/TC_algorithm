'''
두 배열 입력받아서 원소 비교 후 스위칭
'''
n, k = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

for i in range(k):
    if arr_a[i] < arr_b[i]:
        arr_a[i], arr_b[i] = arr_b[i], arr_a[i]
    else:
        break

print(sum(arr_a))