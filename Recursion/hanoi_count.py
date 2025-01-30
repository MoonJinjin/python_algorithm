# 하노이의 탑 이동 수

def hanoi(n: int) -> int:
    if n < 1:
        return 0
    return (hanoi(n - 1) * 2) + 1

n = int(input('정수를 입력하세요: '))
print(hanoi(n))