#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

largestprimefactor = 0
smallestprimefactor = 0
limit = 600851475143
#limit = 100
'''
j = 2
while j <= limit:
	prime = True
	if limit % j == 0:
		print (str(j) + " is a factor")
		counter = 2
		while counter < j:
			if j % counter == 0:
				prime = False
				print (str(j) + " is not prime")
				break
			counter = counter + 1
		if prime == True:
			smallestprimefactor = j 		
			print ("Smallest prime factor: " + str(smallestprimefactor))
			break
	j = j + 1'''

#largestfactor = limit / smallestprimefactor

#print ("Largest factor: " + str(largestfactor))

i = 6935222310
print("go!")
while i <= limit:
	prime = True
	#print ("Looking at " + str(i))
	if limit % i == 0:
		#print (str(i) + " is a factor")
		counter = 2
		while counter < i:
			if i % counter == 0:
				prime = False
				#print (str(i) + " is not prime")
				break
			counter = counter + 1
		if prime == True:
			largestprimefactor = i 		
			print ("Largest prime factor: " + str(largestprimefactor))
			break	
	i = i - 1

