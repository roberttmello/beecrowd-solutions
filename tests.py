def multiply(n: int) -> int:
    return n * 2


values = [1, 2, 3, 4, 5]

multiply_values = map(multiply, values)

print(list(multiply_values))
