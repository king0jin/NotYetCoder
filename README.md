# NotYetCoder
I'm not good at coding. But one day I'll...

## 1단계
### 입출력과 사칙연산
+ 출력 : print()
+ 입력 : input()
+ 공백으로 구분 : .split(" ")
+ 여러 줄 출력 : print(""""""), print('''''')
+ 이스케이프 시퀀스
  + \n : 줄바꿈
  + \t : 탭
  + \\" : 큰따옴표를 문자열 안에서 사용
  + \\\ : 백슬래귀 자체를 출력할 때
 
## 2단계
### 조건문 
+ if:
+ elif:
+ else:
+ match 기준: ~ case 기준값:
+ 여러 데이터/함수를 순차적으로 적용 : map()
+ 시간 계산 - 60으로 나눈 나머지와 몫

## 3단계
### 반복문
반복문에서 **_**는 **임시 변수**로 사용한다
+ i가 1부터 10까지 반복 - **for _ range(1, 10+1):**
+ 시퀀스 객체 순회 - **for _ in 시퀀스객체:**
+ + 리스트 선언 - **리스트이름 = []**
  + 리스트같은 객체를 **시퀀스 객체**라고 한다
+ 리스트에 값 추가 - **.append()**
+ 입력이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다 - **sys.stdin.readline().rstrip()**
#### EOFError란?
프로그램이 예상치 못하게 파일 끝(EOF: End of File)을 만났을 때 발생하는 Error이다
+ 여러 줄을 입력 받을 때 발생할 수 있다
#### 해결방법
+ **try ~ expect** 구문을 사용하여 EOFError가 발생하면 코드를 종료하게 하자 
