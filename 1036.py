import math

input_variables = input().split()

a = float(input_variables[0])
b = float(input_variables[1])
c = float(input_variables[2])
r1, r2 = 0, 0

delta = b * b - (4 * a * c)

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
