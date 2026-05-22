

try:
    temp_dig = int(input("Digite a temperatura em ºC: "))
    temp_f = (temp_dig * (9/5)) + 32

    inf_temp = f'A sua temperatura em ºC é: {temp_dig}\nA sua temperatura em ºF é: {temp_f}'
    msg = 'O clima está '
    
    if temp_dig < 0:
        print(f'{inf_temp}\n{msg}Muito Frio')

    elif temp_dig >= 0 and temp_dig <= 15 :
        print(f'{inf_temp}\n{msg}Frio')

    elif temp_dig >= 16 and temp_dig <= 25 :
        print(f'{inf_temp}\n{msg}Agradável')   

    elif temp_dig >= 26 and temp_dig <= 35 :
        print(f'{inf_temp}\n{msg}Quente') 

    elif temp_dig >= 35:
        print(f'{inf_temp}\n{msg}Muito Quente')   

except ValueError:
    print("O valor digitado é inválido")
else:
    print()
finally:
    print('Encerrando a aplicação')