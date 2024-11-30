#별찍기 6
#   *
#  ***
# *****

N = 1
star = "*"
space = " "

for i in range(3, 0, -1):
    print(space*i, star*N, sep="")
    N += 2