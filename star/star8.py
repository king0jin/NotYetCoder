#별찍기 8
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

N = 9
star = "*"
space = " "
starcount = 1
spacecount = 5


for i in range(1, N+1):
    if i >= 1 and i < 5:
        print(space*spacecount, star*starcount, sep="")
        spacecount -= 1
        starcount += 1
    elif i >= 5 and i < N+1:
        print(space*spacecount, star*starcount, sep="")
        starcount -= 1
        spacecount += 1