# 버블 정렬 알고리즘 (스캔 범위를 제한)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0

    while k < n - 1:
        last = n - 1

        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1] # 패스 과정
                last = j
        k = last


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