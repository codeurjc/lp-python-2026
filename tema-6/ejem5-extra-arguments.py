def strange_func(a, b, *args):
    print(f"a: {a}")
    print(f"b: {b}")
    for arg in args:
        print(f"arg: {arg}")

strange_func(1, 2, 3, 4, 5)

strange_func(1, 2, [3, 4, 5])

strange_func(1, 2, *[3, 4, 5])

###################################3

def strange_func2(a, b, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

strange_func2(1, 2, c=3, d=4, e=5)

strange_func2(1, 2, **{"c": 3, "d": 4, "e": 5})

# Error!!
# strange_func2(1, 2, 3, 4)

###################################

def strange_func3(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    for arg in args:
        print(f"arg: {arg}")
    for k, v in kwargs.items():
        print(f"{k}: {v}")

strange_func3(1, 2, 3, 4, c=5, d=6)

strange_func3(1, 2, *[3, 4], **{"c": 5, "d": 6})

numeros = [1, 2, 3, 4, 5]
cosas_nombradas = {"c": 6, "d": 7, "e": 8}

strange_func3(0, 0, *numeros, **cosas_nombradas)
