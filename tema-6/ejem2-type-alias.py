Vector = list[float]

def scalar_product(scalar: float, v: Vector) -> float:
    return [scalar * x for x in v]

result = scalar_product(2.0, [1.0, -4.2, 5.4])
print(result)