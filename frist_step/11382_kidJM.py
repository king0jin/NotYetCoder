#1-11382번 
#꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 
#이제 A + B + C를 계산할 차례이다!

#  입력
## 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.
## 77 77 7777

#출력
## A+B+C의 값을 출력한다.
## 7931

#구현
numbers = input().split(" ")
A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])
print(A + B + C)