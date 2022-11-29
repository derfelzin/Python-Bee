semana = ('domingo','segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')
dia = str(input())
num = int(input())
if num == 0:
    print('chega hoje!')
elif dia == 'domingo':
    if num == 1:
        print(f'sera entregue {semana[1]}')
    if num == 2:
        print(f'sera entregue {semana[2]}')
    if num == 3:
        print(f'sera entregue {semana[3]}')
    if num == 4:
        print(f'sera entregue {semana[4]}')
    if num == 5:
        print(f'sera entregue {semana[5]}')
    if num == 6:
        print(f'sera entregue {semana[6]}')
elif dia == 'segunda':
    if num == 1:
        print(f'sera entregue {semana[2]}')
    if num == 2:
        print(f'sera entregue {semana[3]}')
    if num == 3:
        print(f'sera entregue {semana[4]}')
    if num == 4:
        print(f'sera entregue {semana[5]}')
    if num == 5:
        print(f'sera entregue {semana[6]}')
    if num == 6:
        print(f'sera entregue {semana[0]}')
elif dia == 'terca':
    if num == 1:
        print(f'sera entregue {semana[3]}')
    if num == 2:
        print(f'sera entregue {semana[4]}')
    if num == 3:
        print(f'sera entregue {semana[5]}')
    if num == 4:
        print(f'sera entregue {semana[6]}')
    if num == 5:
        print(f'sera entregue {semana[0]}')
    if num == 6:
        print(f'sera entregue {semana[1]}')
elif dia == 'quarta':
    if num == 1:
        print(f'sera entregue {semana[4]}')
    if num == 2:
        print(f'sera entregue {semana[5]}')
    if num == 3:
        print(f'sera entregue {semana[6]}')
    if num == 4:
        print(f'sera entregue {semana[0]}')
    if num == 5:
        print(f'sera entregue {semana[1]}')
    if num == 6:
        print(f'sera entregue {semana[2]}')
elif dia == 'quinta':
    if num == 1:
        print(f'sera entregue {semana[5]}')
    if num == 2:
        print(f'sera entregue {semana[6]}')
    if num == 3:
        print(f'sera entregue {semana[0]}')
    if num == 4:
        print(f'sera entregue {semana[1]}')
    if num == 5:
        print(f'sera entregue {semana[2]}')
    if num == 6:
        print(f'sera entregue {semana[3]}')
elif dia == 'sexta':
    if num == 1:
        print(f'sera entregue {semana[6]}')
    if num == 2:
        print(f'sera entregue {semana[0]}')
    if num == 3:
        print(f'sera entregue {semana[1]}')
    if num == 4:
        print(f'sera entregue {semana[2]}')
    if num == 5:
        print(f'sera entregue {semana[3]}')
    if num == 6:
        print(f'sera entregue {semana[4]}')
elif dia == 'sabado':
    if num == 1:
        print(f'sera entregue {semana[0]}')
    if num == 2:
        print(f'sera entregue {semana[1]}')
    if num == 3:
        print(f'sera entregue {semana[2]}')
    if num == 4:
        print(f'sera entregue {semana[3]}')
    if num == 5:
        print(f'sera entregue {semana[4]}')
    if num == 6:
        print(f'sera entregue {semana[5]}')