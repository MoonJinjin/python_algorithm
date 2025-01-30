# 피보나치 수열

def fibo(n: int) -> int:
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

n = int(input('정수를 입력하세요: '))
print(fibo(n))