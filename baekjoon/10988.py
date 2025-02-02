# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

str = input()
check = True
for index, s in enumerate(str):
    if s != str[len(str)-index-1]:
        print(0)
        check = False
        break
if check:
    print(1)