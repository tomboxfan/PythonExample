# 0 is False, non 0 is True ------------
a = bool(0)
b = bool(42)
c = bool(-1)
d = bool(0.0)
e = bool(0.207)
f = bool(-1.117)
print(a, b, c, d, e, f)


# empty list is False, non empty list is True -----
g = bool([])
h = bool([1,5,9])
print(g, h)


# empty string is Flase, non empty string is True --------
i = bool('')
j = bool("Spam")
print(i, j)