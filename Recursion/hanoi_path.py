# 하노이의 탑

def hanoi(n: int, src: int, dst: int) -> int:
    if n < 1:
        return 0

    if src != 0 and dst != 0:
        hanoi(n - 1, src, 0)
    
    if src != 1 and dst != 1:
        hanoi(n - 1, src, 1)
    
    if src != 2 and dst != 2:
        hanoi(n - 1, src, 2)
    
    print(f'{src}에서 {dst}로 옮겼습니다')
    
    if src != 0 and dst != 0:
        hanoi(n - 1, 0, dst)
    
    if src != 1 and dst != 1:
        hanoi(n - 1, 1, dst)
    
    if src != 2 and dst != 2:
        hanoi(n - 1, 2, dst)

hanoi(3, 0, 2)