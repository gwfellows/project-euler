def squareofsum(num, product):
	while num > 1:
		product = product + num
		num = num - 1
		print(product)
	return (product + 1) ** 2

product = 0
num = 100
a = squareofsum(num, product)
print(a)

def sumofsquare(num2, product2):
	while num2 > 1:
		product2 = product2 + (num2 ** 2)
		print (product2)
		num2 = num2 - 1
	return product2 + 1

product2 = 0
num2 = 100
b = sumofsquare(num2, product2)
print(b)
print
print(a - b)

