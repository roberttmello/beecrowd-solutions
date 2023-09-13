input_values_quantity = int(input())
values = []
count_in = 0
count_out = 0

for i in range(input_values_quantity):
    x = int(input())
    values.append(x)

for value in values:
    if 10 <= value <= 20:
        count_in += 1
    else:
        count_out += 1

print(f"{count_in} in")
print(f"{count_out} out")
