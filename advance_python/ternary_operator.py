# numbers list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bool_list = []
# Simple way of ternary operator
for i in number:
    val = True if i % 2 == 0 else False
    bool_list.append(val)
print("Simple way of ternary operator and list output is : {}".format(bool_list))

# Ternary operator using list comprehension
evens = [True if i % 2 == 0 else False for i in number]
print("List comprehension way of ternary operator and list output is: {}".format(evens))
