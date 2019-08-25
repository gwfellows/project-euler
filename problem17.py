'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.'''

strnum = ''
a = ''
b = ''
totallength = 0
num2 = ''

numlist = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'}

def lenofnum(num):
	num = str(num)

	if len(num) == 1:
		strnum = numlist[int(num)]
	
	if len(num) == 2:
		if int(num) <= 19:
			strnum = numlist[int(num)]
			
		if int(num) >= 20:
			if int(num) % 10 == 0:
				strnum = numlist[int(num)]
			else:
				a = num[0]
				b = num[1]
				strnum = numlist[10*int(a)] + numlist[int(b)]
			
	if len(num) == 3:
		a = num[0]
		strnum = numlist[int(a)] + 'hundred'
		if int(num) % 100 != 0:
			strnum = strnum + 'and'
			num = 10 * (int(num[1])) + int(num[2])
			if int(num) <= 19:
				strnum = strnum + numlist[int(num)]
			if int(num) >= 20:
				if int(num) % 10 == 0:
					strnum = strnum + numlist[int(num)]
				else:
					num = str(num)
					a = num[0]
					b = num[1]
					strnum = strnum + numlist[10*int(a)] + numlist[int(b)]
	if len(str(num)) == 4:
		strnum = 'onethousand'
	print(strnum)
	return(len(strnum))

counter = 1
while counter <= 1000:
	totallength += lenofnum(counter)
	counter += 1
	
print(totallength)
