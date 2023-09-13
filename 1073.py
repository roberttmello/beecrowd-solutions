n = int(input())
if n % 2 == 0:
    for i in range(2, n + 2, 2):
        print(f"{i}^2 = {i * i}")
else:
    for j in range(2, n, 2):
        print(f"{j}^2 = {j * j}")
