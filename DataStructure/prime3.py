# 1,000 이햐의 소수 나열 (알고리즘 개선2)

counter = 0
ptr = 0                 # 이미 찾은 소수의 개수
prime = [None] * 500    # 소수를 저장하는 배열

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):     # 홀수만 반복
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])

print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')