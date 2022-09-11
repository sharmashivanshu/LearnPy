# Create a number list
lists = [0, 123, 34, 33, 5, 2]

# Get all even numbers from above list and save it to new list
even_list = []
# Conventional way of looping, using for loop
for i in lists:
    if i % 2 == 0:
        even_list.append(i)

print(even_list)

# List Comprehension
evens = [i for i in lists if i % 2 == 0]
print(evens)
