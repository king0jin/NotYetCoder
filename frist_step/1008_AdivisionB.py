#1-1008번 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
## 1 3
## 4 5

#출력
## 첫째 줄에 A/B를 출력한다. 
## 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
## 0.333333333333333333333333333
## 0.8

#구현
inputnumber = input().split(" ")

number1 = int(inputnumber[0])
number2 = int(inputnumber[1])

answer = number1 / number2

print(answer)