'''A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Idea - make number into string, split string into list of letters, reverse list, compare to original'''

a = 999
b = 999

def reverse(s):
	a = ''
	for i in s:
		a = i + a
	return a

palindromes = list()

#palindromes.append("hi")

while b >= 100:

	while a >= 100:
		s = str(a * b)
		print(s)
		s2 = reverse(s)
		print(s2)

		if s == s2:
			print("palindrome")
			palindromes.append(int(s))
		else:
			print("not a palindrome")

		a = a - 1

 	
	b = b - 1
	a = 999


palindromes.sort()
print (palindromes)