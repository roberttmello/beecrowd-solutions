a, b, c = list(map(float, input().split()))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print(f"Perimetro = {a + b + c:.1f}")
else:
    print(f"Area = {((a + b) * c) / 2:.1f}")
