def starts_with_a(w):
    return w.startswith('a')

lista = ["apple", "banana", "avocado", "cherry", "apricot"]
values = filter(starts_with_a, lista)
for value in values:
    print(value)

def filter(predicate, lista):
    filtered_list = []
    for elem in lista:
        if predicate(elem):
            filtered_list.append(elem)
    return filtered_list

print("Mi función filter devuelve: ", filter(starts_with_a, lista))

print("------------------")

import builtins

values = builtins.filter(lambda w: w.startswith('a'), lista)
for value in values:
    print(value)

print("------------------")

def remove(lista, elem):
    if elem in lista:
        lista.remove(elem)
    return lista

lista = [2, 3, 4, 5]
lista2 = remove(lista[:], 3)
print(lista)
print(lista2)

def minmax(a, b):
    if a > b:
        c = b
        b = a
        a = c
        print(a, b)
a = 10
b = 5
minmax(a, b)
print(a, b)

print("------------------")

import math

lista = list(range(0, 181, 10))
print(lista)
cosins = map(lambda x: math.cos(x), lista)
print(list(cosins))

palabras = ["apple", "Banana", "aVoCaDo", "cherry", "apricot"]
mayusculas = map(lambda w: w.upper(), palabras)
lista_mayusculas = list(mayusculas)

print(type(lista_mayusculas))
longitudes = map(lambda w: len(w), lista_mayusculas)
print(list(longitudes))

len_lambda = lambda w: len(x)
longitudes = map(len_lambda, lista_mayusculas)
