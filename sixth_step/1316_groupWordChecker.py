#6-1316번
#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
#예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
#kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
#aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
## 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
## 3
## happy
## new
## year
#---------
## 4
## aba
## abab
## abcabc
## a

#출력
## 첫째 줄에 그룹 단어의 개수를 출력한다.
## 3
#------
## 1

#구현
#set집합 - 중복을 허용하지 않고 순서를 유지하지 않는 데이터 구조
# 중복 제거, 집합 연산, 빠른 조회

import sys

#1. 입력 받을 단어의 갯수
number = int(input()) 

count = 0

for i in range(number):
    #단어를 입력 받는다
    word = sys.stdin.readline().strip()
    #빈set생성
    seen = set()
    #이전 문자가 저장될 빈 변수 생성
    prev_char = None
    #그룹단어 = True
    is_group_word = True

    #2. 입력한 단어의 요소를 하나씩 가져와서 
    for char in word:
        #3. 해당 요소가 이전 요소와 다르다고
        if char != prev_char:
            #4. 해당 요소가 set에 있다면
            if char in seen:  
                #그룹 단어가 아님
                is_group_word = False
                break
            #4. 해당 요소가 set에 없다면 기록
            seen.add(char)
        #3. 해당 요소사 이전 요소와 같다면 변수에 대입
        prev_char = char
    #5. is_group_word = True이면 count +1
    if is_group_word:
        count += 1

#6. 그룹 단어의 개수 출력
print(count)