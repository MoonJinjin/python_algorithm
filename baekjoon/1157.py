# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

str = input().upper()
str_list = list(set(str))

max_list = []
for s in str_list:
    count = str.count(s)
    max_list.append(count)

if max_list.count(max(max_list)) >= 2:
    print("?")
else:
    print(str_list[max_list.index(max(max_list))])