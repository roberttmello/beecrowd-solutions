n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

values = [n1, n2, n3, n4, n5, n6]

count = 0
positive_values_sum = 0
for value in values:
    if value > 0:
        positive_values_sum += value
        count += 1

print(f"{count} valores positivos")
print(f"{positive_values_sum / count:.1f}")
