
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))

print(year, month, day)

totalDays = 0

if month > 1:
    totalDays = 31
if month > 2:
    totalDays += 28
if month > 3:
    totalDays += 31
if month > 4:
    totalDays += 30
if month > 5:
    totalDays += 31
if month > 6:
    totalDays += 30
if month > 7:
    totalDays += 31
if month > 8:
    totalDays += 31
if month > 9:
    totalDays += 30
if month > 10:
    totalDays += 31
if month > 11:
    totalDays += 30


totalDays += day


# check leap year or not -------------
leapYear = False

if    year % 400 == 0      or      ((year % 4 == 0) and (year % 100 != 0))  :
    leapYear = True

if leapYear and month > 2:
    totalDays +=1


# -------------------------------------




print("Total days:", totalDays)


