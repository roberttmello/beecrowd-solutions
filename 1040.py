n1, n2, n3, n4 = list(map(float, input().split()))

average_1 = ((n1*2) + (n2*3) + (n3*4) + n4) / 10

print(f"Media: {average_1:.1f}")

if average_1 >= 7.0:
    print('Aluno aprovado.')
elif average_1 < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5 = float(input())
    print(f"Nota do exame: {n5:.1f}")
    average_2 = (average_1 + n5) / 2
    if average_2 >= 5.0:
        print('Aluno aprovado.')
    elif average_2 <= 4.9:
        print('Aluno reprovado.')
    print(f'Media final: {average_2:.1f}')
