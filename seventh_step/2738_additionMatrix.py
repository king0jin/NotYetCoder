#7-2738번
#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.


#입력
## 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 
## 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

#출력
## 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
# 4 4 4
# 6 6 6
# 5 6 100

#구현
import sys

number = input().split(" ")
N = int(number[0])
M = int(number[1])

Matrix = []

firstmatrix = []
secondmatrix = []
# 1. 첫 번째 행렬 입력하기
for i in range(1, N+1):
    firstMatrixNum = list(map(int, sys.stdin.readline().strip().split(" ")))
    firstmatrix.append(firstMatrixNum)
# print(firstmatrix)

# 2. 두 번째 행렬 입력하기
for j in range(1, N+1):
    secondMatrixNum = list(map(int, sys.stdin.readline().strip().split(" ")))
    secondmatrix.append(secondMatrixNum)
# print(secondmatrix)

# 3. 행렬 합 계산
for i in range(N):
    row = []
    for j in range(M):
        # 두 행렬의 같은 위치의 값을 더함
        row.append(firstmatrix[i][j] + secondmatrix[i][j])
        # print(row)
    Matrix.append(row)
    # print(Matrix)

# 결과 출력
for row in Matrix:
    for num in row:
        print(num, end=" ")
    print()
