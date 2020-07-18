'''
Key point:
    1) if 最后面要用冒号
    2) 一定要区分 = 和 ==
       = 表示 把右边的值赋值给左边
       == 表示 判断 两边的数字是否相等
'''



if True:
    print("It's true!")

if bool("eggs"):
    print("Yes please")

if "eggs":
    print("Yes please!")

h = 42
if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less then 20")
else:
    print("Between 20 and 50")
