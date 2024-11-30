#별찍기 3
#      *
#     **
#    ***
#   ****
#  *****

N = 5
star = "*"
space = " "

for i in range(1, N+1):
    print(space*(N-1), star*i, sep="")
    N -= 1