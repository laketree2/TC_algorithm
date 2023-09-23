#정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)] #키 값에 함수 =정렬 기준, 리스트 데이터 튜플 기준

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)