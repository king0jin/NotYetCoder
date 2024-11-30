#별찍기 5
# *****
#  ***
#   *

N = 5
star = "*"
space = " "

for i in range(0, 3):
    print(space*i, star*N, sep="")
    N -= 2