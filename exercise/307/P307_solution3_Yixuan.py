# From Yixuan
# 两项分成1组，避免了正负号的问题

pi = 0
for i in range(0,10000):
    pi = pi + 4/(4*i + 1) - 4/(4*i+3)

print(pi)