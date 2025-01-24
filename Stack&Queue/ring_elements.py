# 링 버퍼 (지정된 개수만큼만 저장, 오래된 데이터는 버림)

n = int(input('저장할 데이터 개수를 입력하세요: '))
a = [None] * n

cnt = 0
while True:
    a[cnt % n] = int(input(f'{cnt + 1}번째 정수를 입력하세요: '))
    cnt += 1

    retry = input(f'계속 할까요?(Y/N): ')
    if retry not in {'Y', 'y'}:
        break

i = cnt - n
if i < 0: i = 0

while i < cnt:
    print(f'{i + 1}번째 = {a[i % n]}')
    i += 1