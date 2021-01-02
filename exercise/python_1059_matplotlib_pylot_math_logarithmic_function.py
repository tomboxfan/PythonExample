
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 256, 256)


# logarithmic function: 2 to the power y is x
# We know x, now we want to know y
#
# logarithmic function:
#     x       y
#   log2(2) = 1
#   log2(4) = 2
#   log2(8) = 3
#   log2(16) = 4
#   log2(32) = 5
#   log2(64) = 6
#   log2(128) = 7
# ...
#   the meaning of log2(x) is: divide x in 2 pieces, take 1 piece, divide again, see how many times it takes to reach 1.
#
#  Similarly:
# log10(10) = 1
# log10(100) = 2
# log10(1000) = 3
# log10(10000) = 4
#

y = np.log2(x)



plt.title("logarithmic function: y = log2(x)")
plt.plot(x, y)

plt.show()


