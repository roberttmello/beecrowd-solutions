x = int(input())

if x % 2 == 1:
    for _ in range(6):
        print(x)
        x += 2
else:
    x += 1
    for _ in range(6):
        print(x)
        x += 2
