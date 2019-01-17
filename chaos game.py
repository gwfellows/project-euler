import random
import numpy
import matplotlib.pyplot as plt

xlist = list()
ylist = list()

X = random.randint(0, 1000)
xlist.append(X)

Y = random.randint(0, 1000)
ylist.append(Y)

def headsrule (X, Y):
	X += 50
	Y += 50
	return X,Y

def tailsrule (X, Y):
	Y = Y * 0.75
	X = X * 1.0001
	return X,Y

n = 0

while n < 1000:
	coin = random.randint(0,1)
	if coin == 1:
		X,Y = headsrule (X, Y)
		xlist.append(X)
		ylist.append(Y)
		print(X)
		print(Y)
	else:
		X,Y = tailsrule (X, Y)
		xlist.append(X)
		ylist.append(Y)
		print(X)
		print(Y)
	n += 1

plt.plot([xlist], [ylist], 'ro')
plt.show

print ("DONE")