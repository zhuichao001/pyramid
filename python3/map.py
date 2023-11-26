
arr = [1,2,3,4,5,6]

square = [x**2 for x in arr]
print("squere:", square)

even_square = [x**2 for x in arr if x%2==0]
print("even_square:", even_square)

## use filter and map
ev_sqare = map(lambda x: x**2, filter(lambda x: x%2==0, square))
print("even_square:", even_square)
