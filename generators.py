def fibonacci():
    a,b = 0, 1
    while True:
        a,b = b, a + b
        yield a

f = fibonacci()

def generator():
    yield next(f)


g = generator()
print(print(next(g)))




