numbers = [12, 4, 43, 24, 33, 1, 3]


def multiply(x):
    return x * 2


new_list = []
for i in numbers:
    new_list.append(multiply(i))
print(new_list)

# Map function
mapped_list = []
mapped_list = map(multiply, numbers)
# Map function returns map object which is iterable
# Convert to list by type casting
print(list(mapped_list))
