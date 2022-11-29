valor = float(input())
qtd = int(input())
total = valor * qtd
desconto = total * 0.10
desc = (qtd / 100) * total
totalfinal = total - (desc + desconto)

print(f'{total:.2f}')
print(f'{totalfinal:.2f}')