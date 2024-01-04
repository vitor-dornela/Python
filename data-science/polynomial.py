import numpy as np

result = []
for i in range(-3, 4):
    result.append(4*i**3 - 2*i +2)

print(" ".join(map(str, result)))


# Define two polynomials as polynomial objects
poly1 = np.poly1d([-2, 4, 0, -1]) # represents -2x^3 + 4x^2 - 1
poly2 = np.poly1d([1, -4, -2])   # represents x^2 - 4x - 2

result_poly = poly1 * poly2
print("Multiplication using polynomials objects:\n", result_poly)


# Define two polynomials as lists of coefficients
poly1 = np.array([-1, 0, 4, -2])  # inverted, represents -2x^3 + 4x^2 - 1
poly2 = np.array([-2, -4, 1])    # inverted, represents x^2 - 4x - 2

# Multiply the polynomials using np.convolve
result_poly = np.convolve(poly1, poly2, mode='full')

# Print the result
print("Multiplication using arrays:", result_poly)

# Finding roots of a polynomial
coeficients = [1, 3, -1, -3] # represents x^3 + 3x^2 - x - 3
roots = np.roots(coeficients)
print("Roots of the polynomial:", roots) 

