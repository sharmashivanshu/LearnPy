# Sample generator function
def my_gen():
    n = 1
    print('This is first')
    # Generator functions contains yield statements
    yield n

    n += 1
    print('This is second')
    yield n

    n += 1
    print('This is last')
    yield n


# Using next
a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
