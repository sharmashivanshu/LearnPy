x = 4
print(x ** 2)
l = [1, 3, 5, 9]
generator = (x**2 for x in l)  # parenthesis for generator expression
print(generator)
print(next(generator))
print(next(generator))
