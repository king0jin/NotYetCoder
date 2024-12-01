#별찍기 6
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

N = 9
star = "*"
starcount = 5

for i in range(1, N+1):
    if i >= 1 and i < 5:
        print(star*i)
    elif i >= 5 and i < N+1:
        print(star*starcount)
        starcount -= 1
