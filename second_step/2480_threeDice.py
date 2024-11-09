#2-2480번
#1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 세규칙에 따라 상금을 받는 게임이 있다.
# 1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
#예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 
#또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 
#3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
#3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

#입력
## 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
## 3 3 6
## 2 2 2
## 6 2 5

#출력
## 첫째 줄에 게임의 상금을 출력 한다.
## 1300
## 12000
## 600

#구현
inputdicenumbers = input().split(" ")

dicenum1 = int(inputdicenumbers[0])
dicenum2 = int(inputdicenumbers[1])
dicenum3 = int(inputdicenumbers[2])
dicelist = map(int, list(inputdicenumbers))
#세 개가 모두 같은 수 일 때
prize = 0
if dicenum1 == dicenum2 == dicenum3:
    prize = 10000 + (dicenum1*1000) 
#두 개만 같은 수 일 때
elif dicenum1 == dicenum2 != dicenum3:
    prize = 1000 + (dicenum1*100)
elif dicenum1 == dicenum3 != dicenum2:
    prize = 1000 + (dicenum1*100)
elif dicenum2 == dicenum3 != dicenum1:
    prize = 1000 + (dicenum2*100)
#모두 다른 수 일 때
else:
    maxnum = max(dicelist)
    prize = maxnum * 100
print(prize)