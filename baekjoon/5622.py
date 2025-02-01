# 다이얼 전화를 걸기 위해 필요한 최소 시간

str = input()
list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for s in str:
    for i in list:
        if s in i:
            result += list.index(i) + 3

print(result)