#6-2444번
#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

#입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
## 5

#출력
## 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
#     *
#    ***
#   *****
#  *******
# ********* 
#  *******
#   *****
#    ***
#     *

# for i in range(1, N+1):
#     print(star*i)
# print("------------")    
# for i in range(N, 0, -1):
#     print(star*i)
# print("------------") 
# for j in range(N, i-1, -1):
#     print(bin*j, star*i, sep="")
#     i += 1
# print("------------") 
# for j in range(N, i-1, -1):
#     print(bin*j, star*i, sep="")
#     i += 2
# print("------------")
# for i in range(i, N+1, 1):
#     print(bin*i, star*N, sep="")
#     N -= 2

#1. line
#Python은 짝수 정수로 반올림하는 규칙을 적용
#구현
# import math

# inputnumber = int(input())
# N = inputnumber*2-1
# print("N :", N)
# half = N/2
# half = math.floor(half+ 0.5)
# rehalf = math.floor(half+ 0.5)
# print("half :", half)
# print("rehalf :", rehalf)


# bin = " "
# star = "*"

# for i in range(0, half):
#     # print(half, i+1)
#     print(bin*half, star*(2*i+1), sep="")
#     half -= 1

# # print(rehalf) 
# # print(N)
# for j in range(rehalf+1, N+1): # rehalf : 5, N : 9
#     bin_count = j - rehalf - 1  # 공백 개수
#     star_count = (N - j) * 2 + 1  # 별 개수 (점점 줄어듦)
#     print(bin*bin_count, star*star_count, sep="")

inputnumber = int(input("Input number: "))
N = inputnumber * 2 - 1
print("N:", N)

half = N // 2  # 반을 나타내는 중간 값
print("half:", half)

bin = " "
star = "*"

# 상단 삼각형 출력
for i in range(half + 1):  # 0부터 half까지 반복
    bin_count = half - i  # 공백 개수
    star_count = 2 * i + 1  # 별 개수
    print(bin * bin_count + star * star_count)

# 하단 삼각형 출력
for i in range(half):  # 0부터 half-1까지 반복
    bin_count = i + 1  # 공백 개수
    star_count = 2 * (half - i - 1) + 1  # 별 개수
    print(bin * bin_count + star * star_count)
            