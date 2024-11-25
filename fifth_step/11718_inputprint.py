#5-11718번
#입력 받은 대로 출력하는 프로그램을 작성하시오.

#입력
## 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 
## 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.
## Hello
## Baekjoon
## Online Judge


#출력
## 입력받은 그대로 출력한다.
## Hello
## Baekjoon
## Online Judge


#구현

#1. 여러 줄 입력받기
import sys

inputnlines = sys.stdin.readlines()

for i in inputnlines:
    print(i, end="")

#sys.stdin.readlines()는 EOF 신호를 만나기 전까지 프로그램이 멈춘다
#출력할 때는 print의 end=""를 사용해 개행 문자를 중복해서 출력하지 않도록 설정