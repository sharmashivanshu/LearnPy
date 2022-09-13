squareit = lambda x: x * x

print(squareit(5))
# Another example
print((lambda *args: sum(args))(1, 2, 3, 4, 5))

# Filter results with use of lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(lambda x: x % 2 == 0, numbers)))

