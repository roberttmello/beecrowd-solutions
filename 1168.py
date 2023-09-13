quantidade_leds_por_numero = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}

entrada = int(input())
quantidade_leds = []
count_leds = 0

for _ in range(entrada):
    caracteres = input()
    for caractere in caracteres:
        count_leds += quantidade_leds_por_numero[caractere]
    quantidade_leds.append(count_leds)
    count_leds = 0

for quantidade in quantidade_leds:
    print(f"{quantidade} leds")
