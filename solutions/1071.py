initial_value_range = int(input())
end_value_range = int(input())

if initial_value_range > end_value_range:
    initial_value_range, end_value_range = end_value_range, initial_value_range

odd_values_sum = 0

for value in range(initial_value_range + 1, end_value_range):
    if value % 2 == 1:
        odd_values_sum += value

print(odd_values_sum)
