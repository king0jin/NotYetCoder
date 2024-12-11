#7-2566번
#<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
#이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
#예를 들어, 다음과 같이 81개의 수가 주어지면

# 	    1열	2열	3열	4열	5열	6열	7열	8열	9열
# 1행	3	23	85	34	17	74	25	52	65
# 2행	10	7	39	42	88	52	14	72	63
# 3행	87	42	18	78	53	45	18	84	53
# 4행	34	28	64	85	12	16	75	36	55
# 5행	21	77	45	35	28	75	90	76	1
# 6행	25	87	65	15	28	11	37	28	74
# 7행	65	27	75	41	7	89	78	64	39
# 8행	47	47	70	45	23	65	3	41	44
# 9행	87	13	82	38	31	12	29	29	80

#이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.

#입력
## 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.
# 3 23 85 34 17 74 25 52 65
# 10 7 39 42 88 52 14 72 63
# 87 42 18 78 53 45 18 84 53
# 34 28 64 85 12 16 75 36 55
# 21 77 45 35 28 75 90 76 1
# 25 87 65 15 28 11 37 28 74
# 65 27 75 41 7 89 78 64 39
# 47 47 70 45 23 65 3 41 44
# 87 13 82 38 31 12 29 29 80

#출력
## 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.
# 90
# 5 7

#구현
MatrixList =[]

Matrix = 2 # 9x9 행렬
N = Matrix
# M = Matrix

import sys

#행
for i in range(0, N):
    #행 값
    numberlist = list(map(int, sys.stdin.readline().strip().split(" ")))
    # MatrixList.append(numberlist)
    if len(numberlist) != N:  # 입력된 숫자가 9개가 아닐 경우
        print("9개의 정수를 입력해야합니다")
        break
    MatrixList.append(numberlist)
    # for j in range(0, M):
    #     # numberlist = list(map(int, sys.stdin.readline().strip().split(" ")))
    #     numberlist = list(map(int, input().strip().split(" ")))
    #     MatrixList.append(numberlist)
# print(MatrixList)

# 최댓값 및 위치 찾기
max_value = -1
max_row, max_col = -1, -1

for i in range(N):
    for j in range(N):
        if MatrixList[i][j] > max_value:
            max_value = MatrixList[i][j]
            max_row, max_col = i + 1, j + 1  # 1부터 시작하는 인덱스

# 결과 출력
print(max_value)
print(max_row, max_col)
