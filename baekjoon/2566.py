# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))

result = arr[0][0]
x, y = 1, 1
for i in range(9):
    if result < max(arr[i]):
        result = max(arr[i])

        for j in range(9):
            if arr[i][j] == max(arr[i]):
                x = i + 1
                y = j + 1

print(result)
print(f'{x} {y}')