# 입력
# 첫째 줄에 N(바구니 개수)와 M(줄 개수)가 주어진다.

# 둘째 줄부터는 바구니의 순서를 역순으로 만드는 방법이 주어진다.
# 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)

# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

# 출력
# 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.

N, M = map(int, input().split(" "))
numbers = [i for i in range(1, N + 1)]

for index in range(M):
    i, j = map(int, input().split(" "))
    temp = numbers[i-1:j]
    temp.reverse()
    numbers[i-1:j] = temp

for index in range(N):
    print(numbers[index], end=" ")