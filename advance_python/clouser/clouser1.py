def foo(msg):
    def p():
        print(msg)
    return p


val = foo("hi")
val()

print('hello')
val()
