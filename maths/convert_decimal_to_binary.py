
def findDigitsInDecimal(n):
	x = []
	while n > 0:
		r = n % 10
		x.append(r)
		n = n / 10

	return x[::-1]


def decimalToBinary(n):
	x = []
	while n > 0:
		r = n % 2
		x.append(r)
		n = n / 2
	return x[::-1]