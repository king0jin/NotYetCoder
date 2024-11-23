#5-2908번
#상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 
#상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
#상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 
#상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수 중 큰 수인 437을 큰 수라고 말할 것이다.
#두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
## 734 893
#----------
## 221 231
#----------
## 839 237

#출력
## 첫째 줄에 상수의 대답을 출력한다.
## 437
#-------
## 132
#-------
## 938

#구현
const = input().split(" ")
fristconst = 0
secondconst = 0

# a = int(input())
# a = int(str(a)[::-1])
# print(a, type(a))

maxnum = 0

if len(const[0]) == 3 and len(const[1]) == 3:
    fristconst = int(str(const[0])[::-1])
    secondconst = int(str(const[1])[::-1])
# print(fristconst, type(fristconst))
# print(secondconst, type(secondconst))
if fristconst > secondconst:
    maxnum = fristconst
else:
    maxnum = secondconst
print(maxnum)

# front = list(map(int,str(fristconst)))
# front[::] = front[::-1]
# print(front, type(front))

# back = list(map(int,str(secondconst)))
# back[::] = back[::-1]
# print(back, type(back))
