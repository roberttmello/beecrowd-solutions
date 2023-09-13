x = int(input())

if x % 2 == 1:
    for i in range(1, x + 1, 2):
        print(i)
else:
    for j in range(1, x, 2):
        print(j)
