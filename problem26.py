'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
#use long division

import math
sequences = []

for n in range(2, 1000):

    dividend = '10000000000000'
    divisor = str(n)
    quotient = ''
    remainder = ''
    
    problems_done = []

    pos = 0

    for pos in range(10000):

        if pos == 0:
            quotient += str(int(dividend[pos])  //  int(divisor))
            problems_done.append(dividend[pos] + ' / ' + divisor)
            remainder = str(int(dividend[pos]) % int(divisor))
        else:

            quotient += str(int(remainder) // int(divisor))

            if (remainder + ' / ' + divisor) in problems_done:
                break

            problems_done.append(remainder + ' / ' + divisor)
            remainder = str(int(remainder) % int(divisor))

        try:
            remainder += dividend[pos+1]
        except:
            dividend += '0'
            remainder += dividend[pos+1]

    sequences.append(quotient)


print(max(enumerate(sequences), key=lambda x: len(x[1]))[0] + 2 ) 




