import math


# Point1) Variable definition
userInputStr = input("Please input a number:")

# Point 2) Use variable

# Convert String into int
# Variable definition
userInputInt = int(userInputStr)
print(userInputInt)

# Variable definition
sqrRoot = math.sqrt(userInputInt)

# Use variable
# 把小数小数点后面的数字，删掉
sqrRootInt = int(sqrRoot)

# == 和 =
# == 判断左右两边的数字是不是一样 equals or not
# = assign value
if sqrRootInt == sqrRoot:
    print(userInputStr, "is a square number.")
else:
    print(userInputStr, "is NOT a square number.")
