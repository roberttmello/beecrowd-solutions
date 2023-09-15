maior_valor = 0
posicao_maior_valor = -1

for i in range(1, 101):
    entrada = int(input())
    if entrada > maior_valor:
        maior_valor = entrada
        posicao_maior_valor = i

print(maior_valor)
print(posicao_maior_valor)
