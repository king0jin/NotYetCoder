#4-5597번
#X대학 M교수님은 프로그래밍 수업을 맡고 있다. 
#교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
#교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

#입력
## 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
# 3
# 1
# 4
# 5
# 7
# 9
# 6
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30

#출력
## 출력은 2줄이다. 
## 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
# 2
# 8

#구현

#출석부 30번
students = 30
studentlist = []
for i in range(0, 30):
    studentlist.append(i+1)

#1. 과제를 제출한 번호를 입력
submittedlist = []
for j in range(0, 28):
    submitted = int(input())
    submittedlist.append(submitted)

#2. 과제를 제출하지 않는 번호를 출력
#studentlist와 submittedlist비교하여 없는 번호를 크기순으로 출력
notsubmittedlist = []
for k in studentlist:
    if k in submittedlist:
        continue
    else:
        notsubmittedlist.append(k)

#오름차순으로 정렬
notsubmittedlist.sort()

for g in notsubmittedlist:
    print(g, end=" ")