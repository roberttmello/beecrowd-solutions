salary = float(input())


def get_increase_salary(percentage_increase: float, current_salary: float):
    increase_amount_salary = percentage_increase / 100 * salary
    new_salary_amount = current_salary + increase_amount_salary
    return percentage_increase, increase_amount_salary, new_salary_amount


if 0 <= salary <= 400.00:
    percentage, increase_amount, new_salary = get_increase_salary(15, salary)
elif 400.01 <= salary <= 800.00:
    percentage, increase_amount, new_salary = get_increase_salary(12, salary)
elif 800.01 <= salary <= 1200.00:
    percentage, increase_amount, new_salary = get_increase_salary(10, salary)
elif 1200.01 <= salary <= 2000.00:
    percentage, increase_amount, new_salary = get_increase_salary(7, salary)
else:
    percentage, increase_amount, new_salary = get_increase_salary(4, salary)

print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {increase_amount:.2f}")
print(f"Em percentual: {percentage} %")
