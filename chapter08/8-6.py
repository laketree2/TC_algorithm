'''
개미전사
ㅁ실패코드 - 최댓값을 꼭 포함하지 않아도 되는 반례 존재

최댓값 = 가장 큰 값과 그 차선
가장 큰 값을 구한 후, 그와 인접하지 않은 값 중 
가장 큰 값이 최댓값이 될 것
0값을 가진 리스트를 생성한 후 식량의 개수를 받아 값을 넣음
리스트를 순회하면서 최대값을 찾을 경우 리스트 안에 저장한 후 팝
그 다음 최댓값을 찾아 최초의 최댓값과 자리가 인접하는지 확인한 후 
팝 해서 인덱스에 저장
최종적으로 팝한 값을 더해 출력
'''
#실패한 코드

n = int(input())

arr = list(map(int, input().split()))
n_list = []

# arr.pop(1)
# arr.insert(1, 1)
for i in range(2):
    std = max(arr)
    idx_std = arr.index(max(arr))
    n_list.append(std)
    arr.pop(idx_std)
    if idx_std != arr[0]:
        arr.pop(idx_std-1)
        print('가장 앞', arr)
    if idx_std != len(arr)-1:
        arr.pop(idx_std+1)
        print('가장 뒤', arr)

print(n_list[0]+n_list[1])
