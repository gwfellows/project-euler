'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century 
(1 Jan 1901 to 31 Dec 2000)?
'''

def isleap(y):
	if y % 100 == 0:
		if y % 400 == 0:
			return True
		else:
			return False
	else: 
		if y % 4 == 0:
			return True
		else:
			return False


		
result = isleap(1999)

day = 1
dayofweek = 1
month = 1
year = 1900

answer = 0

'''
1 jan = 31
2 feb = 28 #29 in leap
3 mar = 31
.4 apr = 30
5 may = 31
.6 jun = 30
7 jul = 31
8 aug = 31
.9 sep = 30
10 oct = 31
.11 nov = 30
12 dec = 31
'''

while year <= 2000 and month <= 12 and day <= 31:
	day += 1
	dayofweek += 1
	if month == 2 and day > 28:
		day = 1
		month += 1
	if month == 2 and isleap(year) == True and day > 29:
		day = 1
		month += 1
	if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
		day = 1
		month += 1
	if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day > 31:
		day = 1
		month += 1
	if dayofweek > 7:
		dayofweek = 1
	if month > 12:
		month = 1
		year += 1
	print("day: " + str(day))
	print("dayofweek: " + str(dayofweek))
	print("month: " + str(month))
	print("year: " + str(year))
	print("    ")
	if year >= 1901 and day == 1 and dayofweek == 7:
		answer += 1


print (answer)