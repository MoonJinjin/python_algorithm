# 버블 정렬 알고리즘 (교환 횟수에 따른 중단)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(n - 1):
        exchange = 0 # 패스에서 교환 횟수
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1] # 패스 과정
                exchange += 1
        if exchange == 0: # 마지막 패스를 종료한 시점에서 0이면 정렬을 마친 것
            break


if __name__ == '__main__':
    print('버블 정렬')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')