#별찍기 9
#     *
#    ***
#   *****
#  *******
# ********* 
#  *******
#   *****
#    ***
#     *

N = 9
star = "*"
space = " "
starcount = 1
spacecount = 4

for i in range(1, N+1):
    if i >= 1 and i < 6:
        print(space*spacecount, star*starcount, sep="")
        spacecount -= 1
        starcount += 2
    elif i >= 6 and i <= N+1:
        starcount -= 2
        backstarcount = starcount
        backstarcount -= 2
        spacecount += 1
        backspacecount = spacecount
        backspacecount += 1
        print(space*backspacecount, star*backstarcount, sep="")
