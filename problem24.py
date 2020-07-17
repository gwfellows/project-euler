'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

#notes:
#see https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

# Find the largest index k such that a[k] < a[k + 1].
def findK(a):
    k = len(a) - 2
    while k > 0:
        if a[k] < a[k + 1]:
            return k
        k -= 1
    return k

# Find the largest index l greater than k such that a[k] < a[l].
def findL(a, k):
    l = len(a) - 1
    while l > k:
        if a[k] < a[l]:
            return l
        l -= 1
    return l

# Swap the value of a[k] with that of a[l].
def swap(k, l):
    global a
    a[k], a[l] = a[l], a[k]

def reverse(start, stop):
    global a
    size = stop + start
    for i in range(start, (size + 1) // 2 ):
        j = size - i
        a[i], a[j] = a[j], a[i]

# Reverse the sequence from a[k + 1] up to and including the final element a[n]
def reverseN(k):
    global a
    reverse(k+1, len(a)-1)

num = 0

a = list(range(0,10))

while num <= 1000000-2:
    # print(a)
    k = findK(a)
    # print(a)
    # print("-")
    l = findL(a, k)
    swap(k, l)
    reverseN(k)
    #print(a)
    num += 1


print("".join(map(str, a)))