def lattice_paths(n):
	'''
	Returns the number of paths through a n x n grid
	Makes use of the binomial coefficients from Pascal's triangle
	'''
	num = 1
	for i in range(1,2*n + 1):
		num *= i

	denom = 1
	for j in range(1, n+1):
		denom *= j

	return num / denom**2
