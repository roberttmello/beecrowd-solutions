quantidade_entrada = int(input())
valor = 0
output_values = []

for i in range(quantidade_entrada):
    valor = int(input())
    if valor == 0:
        output_values.append('NULL')
    elif valor > 0:
        if valor % 2 == 0:
            output_values.append('EVEN POSITIVE')
        else:
            output_values.append('ODD POSITIVE')
    else:
        if valor % 2 == 0:
            output_values.append('EVEN NEGATIVE')
        else:
            output_values.append('ODD NEGATIVE')

for value in output_values:
    print(value)
