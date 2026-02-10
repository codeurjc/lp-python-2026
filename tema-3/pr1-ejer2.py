lista1 = [1, 2, 2, 3, 4]
lista2 = [3, 4, 4, 5, 5, 6]

union = []
visited = []
for elem in lista1:
    if elem in lista2:
        if elem not in visited:
            union.append(elem)
    else:
        if elem not in visited:
            union.append(elem)
    visited.append(elem)
for elem in lista2:
    if elem not in visited:
        union.append(elem)
        visited.append(elem)

print("Unión: ", union)

interseccion = []
visited = []
for elem in lista1:
    if elem in lista2 and elem not in visited:
        interseccion.append(elem)
        visited.append(elem)

print("Intersección: ", interseccion)

diferencia = []
visited = []
for elem in lista1:
    if elem not in lista2 and elem not in visited:
        diferencia.append(elem)
        visited.append(elem)

print("Diferencia: ", diferencia)

diferencia_simetrica = []
visited = []
for elem in lista1:
    if elem not in lista2 and elem not in visited:
        diferencia_simetrica.append(elem)
        visited.append(elem)
for elem in lista2:
    if elem not in lista1 and elem not in visited:
        diferencia_simetrica.append(elem)
        visited.append(elem)

print("Diferencia simétrica: ", diferencia_simetrica)

print(set(lista1) | set(lista2))

assert union == list(set(lista1) | set(lista2))
assert interseccion == list(set(lista1) & set(lista2))
assert diferencia == list(set(lista1) - set(lista2))
assert diferencia_simetrica == list(set(lista1) ^ set(lista2))

