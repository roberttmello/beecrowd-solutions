value = float(input())
amount = 0

bills = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for bill in bills:
    amount = int(value / bill)
    print(f'{amount} nota(s) de R$ {bill:.2f}')
    value = value % bill

print("MOEDAS:")
for coin in coins:
    amount = int(round(value,2) / coin)
    print(f'{amount} moeda(s) de R$ {coin:.2f}')
    value = value % coin
