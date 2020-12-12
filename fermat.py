import gmpy2

def fermat_factor(n):
	assert n % 2 != 0

	a = gmpy2.isqrt(n)
	b2 = gmpy2.square(a) - n

	for i in range(100000000):
		a += 1
		b2 = gmpy2.square(a) - n

		if gmpy2.is_square(b2):
			p = a + gmpy2.isqrt(b2)
			q = a - gmpy2.isqrt(b2)

			return True,(int(p), int(q))
	return False,()
#
# print(fermat_factor(0x4e733febb94db17ca3e6aa26ec33b4960c150c52300e06c60b3318f0744fef2d687a8f5bf598894a22eec4abdae01b197e4cc5603de67eb670e261eb4e4cc5e26241edcde494cce415bbc5a410abcefdff6199bbcdf62e9d434faa88a1d16012520f80d126208206ff80191e20ed7423cdce5b8a555b4161534e789a74f0a701))