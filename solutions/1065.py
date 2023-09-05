n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

valores = [n1, n2, n3, n4, n5]
cont_pares = 0

for valor in valores:
    if valor % 2 == 0:
        cont_pares += 1
print(f"{cont_pares} valores pares")
