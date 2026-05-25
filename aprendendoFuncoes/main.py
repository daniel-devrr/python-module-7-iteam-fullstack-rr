# main.py
import menu

def iniciar_programa():
    menu.tela_de_entrada()
    
    while True:
        opcao = menu.obter_opcao()
        
        if opcao == 1:
            menu.fluxo_calculo()
        elif opcao == 0:
            print("\nSaindo do app... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Garante que o programa só roda se executarmos o main.py diretamente
if __name__ == "__main__":
    iniciar_programa()
