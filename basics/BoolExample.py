# 0 is False, non 0 is True ------------
a = bool(0)
b = bool(42)
c = bool(-1)
d = bool(0.0)
e = bool(0.207)
f = bool(-1.117)

# You can print multiple values, separated by comma
print(a, b, c, d, e, f)


# empty list is False, non empty list is True -----
# ignore this if 还没有学list
g = bool([])
h = bool([1,5,9])
print(g, h)


# empty string is Flase, non empty string is True --------
i = bool('')
j = bool("Spam")
print(i, j)


#   >   <   !=      ==  用法
valueEquals1 =  2 == 3
valueEquals2 =  2 < 3
valueEquals3 =  2 > 3
valueEquals4 =  2 != 3
print(valueEquals1, valueEquals2, valueEquals3, valueEquals4)