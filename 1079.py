casos_teste = int(input())
medias = []

for _ in range(casos_teste):
    n1, n2, n3 = list(map(float, input().split()))
    media = (((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10.0)
    medias.append(media)

for media in medias:
    print(f'{media:.1f}')
