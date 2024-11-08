#1-10869번 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

#입력
## 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
## 7 3

#출력
## 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
## 10
## 4
## 21
## 2
## 1

#구현
inputnumber = input().split(" ")

number1 = int(inputnumber[0])
number2 = int(inputnumber[1])

plus = number1 + number2
minus = number1 - number2
multi = number1 * number2
div = number1 % number2

print(plus, minus, multi, div, sep='\n')