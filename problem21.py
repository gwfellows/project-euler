'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10 000.
'''
import math

def d(n):
    result = 1
    for i in range(2,math.ceil(math.sqrt(n))):
        if n%i == 0:
            if i == n/i:
                result += i
            else:
                result += (i + n/i)
    return result

def isAmicable(a, b):
    if d(a) == b and d(b) == a and a != b:
        return True
    else:
        return False

numbersToSearch = list(range(0,10000))

answer = 0

for a in numbersToSearch:
    print(a)
    if a%2 == 0:
        for b in numbersToSearch:
            if b%2 != 0:
                pass
            elif isAmicable(a,b) == True:
                answer += a + b
                numbersToSearch.remove(b)
    elif a%2 != 0:
        for b in numbersToSearch:
            if b%2 == 0:
                pass
            elif isAmicable(a,b) == True:
                answer += a + b
                numbersToSearch.remove(b)


print(answer)