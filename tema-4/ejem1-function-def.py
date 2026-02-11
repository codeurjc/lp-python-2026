def fibonacci(num_terminos):
    a, b = 0, 1
    while(num_terminos> 0):
        print(a)
        a = b
        b = a + b
        num_terminos -= 1

fibonacci(10)
fibonacci(20)
fibonacci(2.5)

print("Tipo del identificador fibonacci: ", type(fibonacci))
fib = fibonacci
print("Tipo del identificador fib: ", type(fib))

fib(4)

print("------------------")

def fibonacci2(num_terminos):
    a, b = 0, 1
    lista_num_terminos = []
    while(num_terminos > 0):
        lista_num_terminos.append(a)
        a = b
        b = a + b
        num_terminos -= 1
    return lista_num_terminos

primeros_10_terminos = fibonacci2(10)
print(primeros_10_terminos)
for value in primeros_10_terminos:
    print(value)

print("------------------")

def minmax(a, b):
    if a < b:
        return a, b
    else:
        return b, a

min, max = minmax(5, 10)
print(min, max)

min = minmax(5, 10)
print(min)
print(type(min))

def div(dividendo, divisor):
    return dividendo / divisor, dividendo // divisor, dividendo % divisor

real, cociente, resto = div(10, 3)
print(real, cociente, resto)
resultado = div(10, 3)
print(resultado)
cociente, resto = div(10, 3)[1:3]
print(cociente, resto)

print("------------------")

resutado = div(divisor=3, dividendo=10)
print(resutado)
