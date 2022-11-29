divida = int(input())
pag = int(input())
cont = 1

while divida > 0:

    print(f'pagamento: {cont}')
    print(f'antes = {divida}')
    divida -= pag
    if divida >=0:
        print(f'depois = {divida}')
    else:
        print('depois = 0')
    print('-----')
    cont += 1        