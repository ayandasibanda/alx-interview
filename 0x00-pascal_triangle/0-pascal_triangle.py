def pascal_triangle(n):
	# If n is less than or equal to 0, return an empty list
	if n <= 0:
		return []
	
	# Initialize a list of lists, triangle, with n rows
	# Each row contains i+1 ones (where i is the row number)
	triangle = [[1 for _ in range(i+1)] for i in range(n)]
	
	# Fill in the rest of the triangle using the Pascal's triangle formula
	# Each element is the sum of the two elements directly above it
	for i in range(2, n):
		for j in range(1, i):
			triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
	
	# Return the completed triangle
	return triangle

