names = ['Ram', 'Karan', 'Arjun', 'Ravi', 'Lucky']
ages = [12, 34, 21, 15, 55]

# for names, ages in zip(names, ages):
#     print(f'{names}:{ages}')

# zip returns iterable. Since its already iterated, to make it run following code need to comment above loop
print(list(zip(names, ages)))
