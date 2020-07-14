'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
#notes:
# Every multiple of an abundant number is abundant
# every multiple beyond 1 of a perfect number is abundant
# limit is 20161, not 28123


import math
import itertools

def d(n):
    result = 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            if i == n/i:
                result += i
            else:
                result += (i + n/i)
    return result

abundants = []

nums = list(range(2,20161))

#for i in nums:
#     if d(i) > i:
#         a = i
#         while a <= 20161:
#             abundants.append(a)
#             try:
#                 nums.remove(a)
#             except:
#                 pass
#             a += i
#     elif d(i) == i:
#         a = 2*i
#         while a <= 20161:
#             abundants.append(a)
#             try:
#                 nums.remove(a)
#             except:
#                 pass
#             a += i

for i in range(12, 20162):
    if d(i) > i:
        #print(i)
        abundants.append(i)


nonAbs = [x for x in range(20162)]

for i in range(len(abundants)):
	for j in range(i,20162):
		if abundants[i]+abundants[j] < 20162:
			nonAbs[abundants[i]+abundants[j]] = 0
		else:
			break

print(sum(nonAbs))