#1-2588번 
#(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#         472 (1)
#       x 385 (2)
#    ---------
#        2360 (3)
#       3776  (4)
#      1416   (5)
#    ---------
#      181720 (6)
#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 
#(3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

#  입력
## 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
## 472
## 385

#출력
## 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
## 2360
## 3776
## 1416
## 181720

#구현
numbers = input().split(" ")
#(1)
number1 = int(numbers[0])
#(2)
number2 = numbers[1]
number2_list = list(number2)
if(len(number2_list)==3):
    num1 = int(number2_list[2])
    num2 = int(number2_list[1])
    num3 = int(number2_list[0])

#(3)
answer3 = number1 * num1
#(4)
answer4 = number1 * num2
#(5)
answer5 = number1 * num3

#(6)
answer6 = number1 * int(number2)

print(answer3, answer4, answer5, answer6, sep="\n")
