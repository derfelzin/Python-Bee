number = int(input())
contador = 0

while True:
    if number <=26:
        break

for letra in range(number):
    contador += 1
    print(contador * chr(65+letra))