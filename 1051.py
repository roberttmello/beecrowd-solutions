salario = float(input())
valor_imposto = 0.00

if salario <= 2000.00:
    print("Isento")
elif 2000.01 <= salario <= 3000.00:
    valor_imposto = (salario - 2000.00) * 0.08
    print(f"R$ {valor_imposto:.2f}")
elif 3000.01 <= salario <= 4500.00:
    salario = salario - 2000.00
    valor_imposto = 1000.00 * 0.08
    valor_imposto += (salario - 1000.00) * 0.18
    print(f"R$ {valor_imposto:.2f}")
else:
    salario = salario - 2000.00
    valor_imposto = 1000.00 * 0.08
    valor_imposto += 1500.00 * 0.18
    valor_imposto += (salario - 2500.00) * 0.28
    print(f"R$ {valor_imposto:.2f}")
