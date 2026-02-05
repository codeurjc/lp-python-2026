lista = [2, 3, 4, 5]

print(lista)

print(lista[0])

lista[0] = 1
print(lista)

del lista[0]
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)

lista.append(6)
print(lista)

lista.extend([7, 8, 9])
print("Extended:", lista)

lista.insert(0, 0)
print(lista)

lista.remove(6)
print(lista)

print("Index of value 5:", lista.index(5))

print("Number of 5's:", lista.count(5))

print("Length of list:", len(lista))

print("Biggest element in the list: ", max(lista))

strings = ["ab", "aa", "ba", "baa"]
print("Biggest element in the list of strings: ", max(strings))

print("Smallest element in the list: ", min(lista))

print("Sum of all elements in the list: ", sum(lista))

print(lista[1:3])

print(lista[1:])

print(lista[:3])

print(lista[:])

copy=lista[:]
copy2=lista
print("copy==lista:", copy == lista)
print("copy is the same object than lista:", copy is lista)

print("copy2==lista:", copy2 == lista)
print("copy2 is the same object than lista:", copy2 is lista)

copy[1] = 10
print(copy)
print(lista)

print("copy==lista:", copy == lista)
print("copy is the same object than lista:", copy is lista)

copy = lista[1:3]
copy[0] = 100
print("Copy:", copy)
print("Lista:", lista)

cuadrados = [x**2 for x in range(1, 11)]
print("Cuadrados:", cuadrados)

cuadrados_de_numeros_pares = cuadrados[1::2]
print("Cuadrados de los 10 primeros números pares:", cuadrados_de_numeros_pares)

import math 

cosenos = [math.cos(x) for x in range(0, 180, 5)]
print(cosenos)

print(len(cosenos))

