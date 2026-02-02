ids = {}
ids['peter'] = 1
ids['mia'] = 2

print(ids)
print(ids['peter'])

ids['peter'] = 10
print(ids)

# Uncomment this line to see the error (it stops running the script)
# print(ids['john'])

print(ids.get('john'))

ids['john'] = 5
del ids['peter']
print(ids)

print(ids.items())
print(ids.keys())
print(ids.values())

ids.clear()
print(ids)
