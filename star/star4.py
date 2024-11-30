#별찍기 4
# *****
#  ****
#   ***
#    **
#     *

N = 5
star = "*"
space = " "
# j = 0
# for i in range(N, j, -1):
#     print(space*j, star*i, sep="")
#     j += 1

for i in range(0, N):
    print(space*i, star*N, sep="")
    N -= 1
