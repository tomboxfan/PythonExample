
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 201) # [-10, 10] 生成201个点 (分成200段), 所以-10.0, -9.9, -9.8 ....9.9, 10.0 一共201个数字


# Exponential function: 2 to the power x is y
# We know x, now we want to know y
#
# Exponential function:
#     x       y
#   2^0     = 1
#   2^1     = 2
#   2^2     = 4
#   2^3     = 8
#   2^4     = 16
#   2^5     = 32
#   2^6     = 64
# ...
# y = 2 ** x

plt.title("exponential function: y = 2^x")
plt.plot(x, 2 ** x)       # y= 2^x
plt.plot(x, 3 ** x)       # y= 3^x
plt.plot(x, 4 ** x)       # y= 4^x

plt.show()


