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


# Using for loop
for item in my_gen():
    print(item)
