def div2(dividendo, divisor=2):
    return dividendo / divisor

print(div2(10, 5))
print(div2(10))
# Error: falta al menos un parámetro
# print(div2())
print(div2(dividendo=25))
print(div2(divisor=5, dividendo=25))

def div3(dividendo=10, divisor=2):
    return dividendo / divisor

print(div3())

print("------------------")

def pow(base, exponente=2):
    return base ** exponente

print(pow(27))

print("------------------")

def div4(dividendo, divisor, format=None):
    if format is None:
        return dividendo / divisor
    elif format == "cociente":
        return dividendo // divisor
    elif format == "resto":
        return dividendo % divisor
    else:
        return dividendo, dividendo // divisor, dividendo % divisor

print(div4(10, 3))
print(div4(10, 3, "cociente"))
print(div4(10, 3, "resto"))

def pow2(base, exponente=2, format=None):
    value = base ** exponente
    if format is not None:
        match format:
            case "hexadecimal":
                return hex(value)
            case "octal":
                return oct(value)
            case "binary":
                return bin(value)
            case _:
                return value
    else:
        return value

