casos_de_teste = int(input())
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

for _ in range(casos_de_teste):
    quant_cobaia, caractere_animal = list(map(str, input().split()))
    total_cobaias += int(quant_cobaia)
    if caractere_animal == 'R':
        total_ratos += int(quant_cobaia)
    elif caractere_animal == 'S':
        total_sapos += int(quant_cobaia)
    else:
        total_coelhos += int(quant_cobaia)

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelhos}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {total_coelhos * 100 / total_cobaias:.2f} %')
print(f'Percentual de ratos: {total_ratos * 100 / total_cobaias:.2f} %')
print(f'Percentual de sapos: {total_sapos * 100 / total_cobaias:.2f} %')
