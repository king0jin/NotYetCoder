#3-10951번
#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

#입력
## 입력은 여러 개의 테스트 케이스로 이루어져 있다.
## 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
## 1 1
## 2 3
## 3 4
## 9 8
## 5 2

#출력
## 각 테스트 케이스마다 A+B를 출력한다.
## 2
## 5
## 7
## 17
## 7

#구현1 - EOFError발생
# 두 수를 입력 받는다 - 공백기준으로
# num1에 첫번째 입력 수를 넣는다
# num2에 두번째 입력 수를 넣는다
# num1+num2를 수행해서 sum에 저장해서 출력한다
# 더 이상 입력이 없으면 반복문을 빠져나온다
# while True:
#     numbers = input().split()
#     if not numbers or numbers == ['']:  # 빈 줄 입력 시 종료
#         break
#     num1 = int(numbers[0])
#     num2 = int(numbers[1])
#     sum = num1 + num2
#     print(sum)

#구현2 : try ~ except
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break