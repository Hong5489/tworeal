from Crypto.Util.number import GCD #for gcd function (or easily implementable to avoid import)
import random #for random elements drawing in RecoverPrimeFactors

def failFunction():
	print("Prime factors not found")

def outputPrimes(a, n):
	p = GCD(a, n)
	q = n // p
	if p > q:
		p, q = q, p
	print("Found factors p and q")
	print("p = {0}".format(str(p)))
	print("q = {0}".format(str(q)))
	return p,q


def recover(n, e, d):
	"""The following algorithm recovers the prime factor
		s of a modulus, given the public and private
		exponents.
		Function call: RecoverPrimeFactors(n, e, d)
		Input: 	n: modulus
				e: public exponent
				d: private exponent
		Output: (p, q): prime factors of modulus"""

	k = d * e - 1
	if k % 2 == 1:
		failFunction()
		return 0, 0
	else:
		t = 0
		r = k
		while(r % 2 == 0):
			r = int(r // 2)
			t += 1
		for i in range(1, 101):
			g = random.randint(0, n) # random g in [0, n-1]
			y = pow(g, r, n)
			if y == 1 or y == n - 1:
				continue
			else:
				for j in range(1, t): # j \in [1, t-1]
					x = pow(y, 2, n)
					if x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
					elif x == n - 1:
						continue
					y = x
					x = pow(y, 2, n)
					if  x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q

# n = 0x3A6160848FB1734CBD0FA22CEF582E849223AC04510D51502556B6476D07397F03DF155289C20112E87C6F35361D9EB622CA4A0E52D9CD87BF723526C826B88387D06ABC4279E353F12AD8EC62EA73C47321A20B89644889A792A73152BC7014B80A693D2E58B123FA925C356B1EBA037A4DCAC8D8DE809167A6FCC30C5C785
# e = 0x0365962e8daba7ba92fc08768a5f73b3854f4c79969d5518a078a034437c4669bdb705be4d8b8babf4fda1a6e715269e87b28eecb0d4e02726a27fb8721863740720f583688e5567eb10729bb0d92b322d719949e40c57198d764f1c633e5e277da3d3281ece2ce2eb4df945be5afc3e78498ed0489b2459059664fe15c88a33
# d = 89508186630638564513494386415865407147609702392949250864642625401059935751367507
# print(RecoverPrimeFactors(n,e,d)
