#3-11022번
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#입력
## 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 
## x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
## 5
## 1 1
## 2 3
## 3 4
## 9 8
## 5 2

#출력
## 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
## Case #1: 1 + 1 = 2
## Case #2: 2 + 3 = 5
## Case #3: 3 + 4 = 7
## Case #4: 9 + 8 = 17
## Case #5: 5 + 2 = 7

#구현
import sys
T_lines = int(input())
number1 = []
number2 = []
answerlist = []
for i in range(0, T_lines):
    TwoNumber = sys.stdin.readline().rstrip()
    TwoNumberlist = TwoNumber.split(" ")
    number1.append(int(TwoNumberlist[0]))
    number2.append(int(TwoNumberlist[1]))
    answer = number1[i] + number2[i]
    answerlist.append(answer)
for j in range(0, len(answerlist)):
    print("Case #", j+1, ": ", number1[j], " + ", number2[j], " = ", answerlist[j], sep="")