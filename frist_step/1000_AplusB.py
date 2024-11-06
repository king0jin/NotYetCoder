#1-1000번 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
## 1 2

#출력
## 첫째 줄에 A+B를 출력한다.
## 3

#구현
inputnum = input().split(" ")
number1 = int(inputnum[0])
number2 = int(inputnum[1])

answer = number1 + number2

print(answer)