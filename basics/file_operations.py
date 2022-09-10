

with open('file_test.txt', 'r+') as f:

    f.write("Hello \n World")
    content = f.read()
    print(content)






