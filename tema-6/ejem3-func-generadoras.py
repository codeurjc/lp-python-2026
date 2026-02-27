def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(100):
    print(num)

it = fibonacci(10)
print(type(it))

for num in it:
    print(num)

it = fibonacci(10)
for _ in range(10):
    print(it.__next__())

#print(it.__next__())

for i in range(20):
    print(it.__next__())