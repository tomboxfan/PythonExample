
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))

dayList = [0, # there is 0 full month before Jan
           31, # Feb has 31 days in its previous month
           31 + 28, # Mar
           31 + 28 + 31, # Apr
           31 + 28 + 31 + 30, # May
           31 + 28 + 31 + 30 + 31, # Jun
           31 + 28 + 31 + 30 + 31 + 30, # Jul
           31 + 28 + 31 + 30 + 31 + 30 + 31, # Aug
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31, # Sep
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30, # Oct
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31, # Nov
           31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 # Dec
]

totalDays = dayList[month-1]

leapYear = False

if year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0)):
    leapYear = True

if leapYear and month > 2:
    totalDays +=1

totalDays += day

print("Total days:", totalDays)