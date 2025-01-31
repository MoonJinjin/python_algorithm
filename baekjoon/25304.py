# 입력
# 첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.

# 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

# 출력
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

total = int(input())
totalNum = int(input())

result = 0
for i in range(0, totalNum, 1):
    sum, cnt = map(int, input().split(" "))
    result += sum * cnt

if result == total:
    print("Yes")
else:
    print("No")