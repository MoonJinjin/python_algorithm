# 입력
# 첫 번째 줄에는 문제의 정수 N이 주어진다.

# 출력
# 혜아가 N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

n = int(input())

result = ""
for i in range(0, n, 4):
    result += "long "
result += "int"

print(result)