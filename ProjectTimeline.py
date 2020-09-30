import datetime

days = 0

print("##Project Start Date")
dayStart = int(input("start day : "))
monthStart = int(input("start month : "))
yearStart = int(input("start year : "))

startDate = datetime.datetime(yearStart, monthStart, dayStart)


print("##Project Start Date")
dayEnd = int(input("end day : "))
monthEnd = int(input("end month : "))
yearEnd = int(input("end year : "))

endDate = datetime.datetime(yearEnd, monthEnd, dayEnd)


print((endDate.year - startDate.year) * 365 + (endDate.month - startDate.month) * 30 + (endDate.day - startDate.day), "days")
