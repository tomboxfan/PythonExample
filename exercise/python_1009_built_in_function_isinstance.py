# isinstance() is to check whether some variable is of some type


#shortcut key - Ctrl + Alt + v - extract variable

bool1 = isinstance('hello!', str)
bool2 = isinstance('hello!', int)
print(f"'hello' is of type str? {bool1}")
print(f"'hello' is of type int? {bool2}")

bool3 = isinstance(5, int)
bool4 = isinstance(5, float)
print(f"5 is of type int? {bool3}")
print(f"5 is of type float? {bool4}")