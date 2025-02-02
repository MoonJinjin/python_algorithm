# 입력
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

# 출력
# 치훈이의 전공평점을 출력한다.
# 정답과의 절대오차 또는 상대오차가 10^-4 이하이면 정답으로 인정한다.

grade_list = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

sum = 0
scoreSum = 0
for _ in range(20):
    subject, score, grade = input().split()

    if grade != "P":
        sum += float(score) * grade_list[grade]
        scoreSum += float(score)

print(sum/scoreSum)