#1-10430번 
#(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
#(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
#세 수 A, B, C가 주어졌을 때, 
#위의 네 가지 값을 구하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
## 5 8 4

#출력
## 첫째 줄에 (A+B)%C, 
## 둘째 줄에 ((A%C) + (B%C))%C, 
## 셋째 줄에 (A×B)%C, 
## 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
## 1
## 1
## 0
## 0

#구현
numbers = input().split(" ")
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)