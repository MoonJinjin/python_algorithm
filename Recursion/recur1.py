# 순수한 재귀 함수

def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

x = int(input('정수를 입력하세요: '))

recur(x)