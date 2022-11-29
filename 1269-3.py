def virtual_lista(lista):
    for item in range(len(lista)):
        lista[item] = int(lista[item])

def exibir(carrinho):
    for item in range(len(carrinho)):
        if item < len(carrinho) - 1:
            print(carrinho[item], end=' ')
        else:
            print(carrinho[item])

carrinho = input().split()
if carrinho != []:
    virtual_lista(carrinho)
comando = input().split()
while comando[0] != 'encerrar':
    if comando[0] == 'adicionar':
        carrinho.append(int(comando[1]))
    elif comando[0] == 'remover':
        comando[1] = int(comando[1])
        if comando[1] in carrinho:
            carrinho.remove(comando[1])
        else:
            print(f'código {comando[1]} não encontrado')
    else:
        carrinho.sort()
        exibir(carrinho)
    comando = input().split()
carrinho.sort()
exibir(carrinho)