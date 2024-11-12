#4-10807번
#총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

#입력
## 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 
## 둘째 줄에는 정수가 공백으로 구분되어져있다. 
## 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 
## 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
## 11
## 1 4 1 2 4 2 4 2 3 4 4
## 2
#---------------------
## 11
## 1 4 1 2 4 2 4 2 3 4 4
## 5

#출력
## 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
## 3
#-------------
## 0

#구현
numberlist = []
countdic = {}
count = 0
#1.정수의 개수를 입력한다
num = int(input())
#2. 정수의 개수만큼 정수들을 입력받는다
while True:
    numbers = input().split()
    #만약, 입력한 정수의 개수와 처음에 정한 정수의 개수가 같으면
    if len(numbers) == num:
        #리스트에 넣고 반복문을 빠져나온다
        numberlist = list(map(int, numbers))
        break

#3. 찾고 싶은 정수를 입력한다 
wantnum = int(input())
#4. numberlist를 하나씩(i)조회하는데
for i in numberlist:
    #countdic안에 조회한 i가 없다면
    if i not in countdic:
        #countdic에 넣고 초기화를 한다
        countdic[i] = 0
    #있다면 +1을 한다
    countdic[i] += 1

#5. 찾고 싶은 정수가 있다면 몇개인지 출력한다
if wantnum in countdic:
    print(countdic[wantnum])
else:
    print("0")