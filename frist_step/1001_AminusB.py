#1-1000번 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
## 3 2

#출력
## 첫째 줄에 A-B를 출력한다.
## 1

#구현
inputnumber = input().split(" ")
number1 = int(inputnumber[0])
number2 = int(inputnumber[1])

answer = number1 - number2

print(answer)