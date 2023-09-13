inicio, fim = list(map(int, input().split()))

if inicio == fim:
    print('O JOGO DUROU 24 HORA(S)')
elif fim > inicio:
    print(f'O JOGO DUROU {fim - inicio} HORA(S)')
else:
    print(f'O JOGO DUROU {(fim + 24) - inicio} HORA(S)')
