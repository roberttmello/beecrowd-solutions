n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

values = [n1, n2, n3, n4, n5]

odd_values_count = 0
even_values_count = 0
negative_values_count = 0
positive_values_count = 0

for value in values:
    if value > 0:
        positive_values_count += 1
        if value % 2 == 0:
            even_values_count += 1
        else:
            odd_values_count += 1
    elif value < 0:
        negative_values_count += 1
        if value % 2 == 0:
            even_values_count += 1
        else:
            odd_values_count += 1
    else:
        even_values_count += 1

print(f"{even_values_count} valor(es) par(es)")
print(f"{odd_values_count} valor(es) impar(es)")
print(f"{positive_values_count} valor(es) positivo(s)")
print(f"{negative_values_count} valor(es) negativo(s)")
