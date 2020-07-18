import datetime

year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))

d1 = datetime.date(year, month, day)
d2 = datetime.date(year-1, 12, 31)
print((d1-d2).days)