VicCoin = float(0)
soma_quantidade = 0

while VicCoin !=-1:
    VicCoin = float(input())
    soma_quantidade += VicCoin
    if VicCoin ==-1:
        soma_quantidade +=1
        reais = soma_quantidade * 2.50
        print(f'VC$ {soma_quantidade:.2f}')
        print(f'R$ {reais:.2f}')