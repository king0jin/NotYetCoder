#3-2439번
#첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
#하지만, 오른쪽을 기준으로 정렬한 별을 출력하시오.

#입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
## 5

#출력
## 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
##     *
##    **
##   ***
##  ****
## *****

#구현
lineNum = int(input())

bincan = " "
for i in range(1, lineNum+1): #ex) 총 다섯번 반복문을 돌겠다
    #규칙성
    #공백이 lineNum-1개 + 별:1개
    print(bincan * (lineNum-i) + "*" * i)
    # print("*" * i)
    #공백이 lineNum-2개 + 별:2개
    #공백이 lineNum-3개 + 별:3개
    #공백이 lineNum-4개 + 별:4개
    #공백이 lineNum-5개 + 별:5개
