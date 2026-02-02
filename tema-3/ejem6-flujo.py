# If

a = 2
b = 3

if a == b:
    print('a is equal to b')
elif a > b:
    print('a is greater than b')
else:
    print('a is less than b')

if a != b:
    print('a is not equal to b')

c = 2.0

if a == c and b != c:
    print('a is equal to c')

if not a == b:
    print('a is not equal to b')

if a in [1, 2, 3]:
    print('a is in the list')



# Ternary

print('a is equal to b') if a == b else print('a is not equal to b')

# Match
status = 404
match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")

# point is an (x, y) tuple
point = (2, 0)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

# While

i = 0
while i < 10:
    print(i)
    i += 1

nums = [1, 2, 3, 4, 3, 5, 3]

while 3 in nums:
    nums.remove(3)

print(nums)

# For

for i in range(10):
    print(i)

names = ['mia', 'peter', 'john']
for name in names:
    print(name)

ids = {'mia':1, 'peter':2, 'john':3}
for name, id in ids.items():
    print(name + ':' + str(id))

for id in ids.values():
    print(id)

for name in ids.keys():
    print(name)