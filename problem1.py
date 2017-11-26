#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

multiplesum = 0
mult3 = 0
mult5 = 0

i = 1

multiplelist = list()

def checkduplicates(mult, multiplelist):
	flag = False 
	for item in multiplelist:
		if item == mult:
			flag = True
	return flag


while (mult3 < 1000):
		
	mult3 = 3 * i
	mult5 = 5 * i
	
	if mult3 < 1000 and checkduplicates(mult3, multiplelist) == False:
		multiplelist.append(mult3)
	
	if mult5 < 1000 and checkduplicates(mult5, multiplelist) == False:
		multiplelist.append(mult5)
	
	print ("Counter: " + str(i) + " mult3: " + str(mult3) + " mult5: " + str(mult5))
	
	i = i + 1

for item in multiplelist:
	multiplesum = multiplesum + item
	
print ("Multiple sum: " + str(multiplesum))