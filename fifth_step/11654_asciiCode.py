#5-11654번
#알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

#입력
## 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
# A

#출력
## 입력으로 주어진 글자의 아스키 코드 값을 출력한다.
# 65

#구현
# 파이썬에서는 ord()와 chr() 함수를 통해 문자를 아스키코드로, 아스키코드를 문자로 변환할 수 있다.
#1. 문자를 입력받는다
wonder = input()
#2. 입력받은 문자를 아스키코드 값으로 변환한다 
answer = ord(wonder)
print(answer)