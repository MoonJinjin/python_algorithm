# 하노이의 탑

def move(n: int, x: int, y: int) -> None: # x와 y는 1, 2, 3
    # 원반 n개를 x기둥에서 y기둥으로 옮김
    if n > 1:
        move(n - 1, x, 6 - x - y) # 6 - x - y: 중간 기둥

    print(f'원반 [{n}]를 {x}기둥에서 {y}기둥으로 옮깁니다')

    if n > 1:
        move(n - 1, 6 - x - y, y)

print('하노이의 탑을 구현합니다')
n = int(input('원반의 개수를 입력하세요: '))

move(n, 1, 3)