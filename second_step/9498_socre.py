#2-9498번
#시험 점수를 입력받아 
#90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 
#나머지 점수는 F를 출력하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 시험 점수가 주어진다. 
## 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
## 100

#출력
## 시험 성적을 출력한다.
## A

#구현
input = input()
score = int(input)

if score >= 0 and score <= 100:
    num = score // 10
    match num:
        case 10 | 9:
            print("A")
        case 8:
            print("B")
        case 7:
            print("C")
        case 6:
            print("D")
        case _:
            print("F")
else:
    print("점수를 잘못 입력하셨습니다.")