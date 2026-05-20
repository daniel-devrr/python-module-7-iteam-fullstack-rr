

num_dig = float(input('Digite um número de 1 à 10: '))

for i in range(1, 11):
    resultado = num_dig * i
    print(f'{num_dig} x {i} = {resultado:.2f}')