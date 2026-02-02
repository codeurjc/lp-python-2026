mi_set = set()
mi_set.add(1)
mi_set.add(2)
mi_set.add(3)

print(mi_set)

mi_set.remove(2)
print(mi_set)

mi_set.discard(1)
print(mi_set)

mi_set.clear()
print(mi_set)

uno = {1, 2, 3, 4}
dos = {3, 4, 5, 6}

print(uno | dos)
print(uno & dos)
print(uno - dos)
print(uno ^ dos)

print(2 in uno)
print(2 in dos)