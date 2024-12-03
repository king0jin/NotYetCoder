#6-1157번
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

#입력
## 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
## Mississipi
#------------
## zZa
#------------
## z
#------------
## baaa

#출력
## 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
## ?
#----------
## Z
#----------
## Z
#----------
## A

#구현
word = list(input().upper())

wordcount = {}
count = 1
for i in word:
    if i not in wordcount:
        wordcount[i] = 1
    else:
        wordcount[i] += 1

# print(wordcount)
# print("딕셔너리 길이는", len(wordcount))

# 최댓값과 최댓값에 해당하는 알파벳 리스트
max_count = 0
max_alphabet = []

for key, value in wordcount.items():
    if value > max_count:  # 더 큰 값이 나오면 갱신
        max_count = value
        max_alphabet = [key]  # 새로운 최댓값 알파벳으로 교체
    elif value == max_count:  # 최댓값과 같은 값이 나오면 추가
        max_alphabet.append(key)

# 결과 출력
if len(max_alphabet) == 1:
    print(max_alphabet[0]) 
else:
    print("?")      
