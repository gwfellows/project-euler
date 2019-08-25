'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

def collatz(n):
	length = 0
	while n != 1:
		if n <= len(lengthlist) and len(lengthlist) != 0:
			length = length + lengthlist[int(n)]
			return(length)
		else:
			if n % 2 == 0:
				n = n/2
			else:
				n = 3*n + 1
			length += 1
	length = length + 1
	return(length)

counter = 2
lengthlist = {}

while counter <= 1000000:
	lengthlist[counter] = collatz(counter)
	counter += 1

inverse = [(value, key) for key, value in lengthlist.items()]
print(max(inverse)[1])

#print(lengthlist)

