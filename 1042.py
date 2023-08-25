my_values = list(map(int, input().split()))
my_values_copy = my_values.copy()
my_values.sort()
for value in my_values:
    print(value)
print()
for value_copy in my_values_copy:
    print(value_copy)
