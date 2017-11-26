# Problem 6

def sum(num, product):
	while num > 1:
		product = product + num
		print (product)
		num = num - 1
	return product

product = 1
num = 100
a = sum(num, product)
print(a)