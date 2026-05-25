# menu.py
# Importa as funções que criamos no outro arquivo
import calculos 

def tela_de_entrada():
    print("================================")
    print(" Seja bem-vindo ao Calcule Seu IMC ")
    print("================================")

def obter_opcao():
    return int(input("\nDigite 1 para calcular ou 0 para Sair: "))

def fluxo_calculo():
    print("\n--- NOVO CÁLCULO ---")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    # Usando as funções do arquivo calculos.py
    resultado_imc = calculos.calcular_imc(peso, altura)
    status = calculos.classificar_imc(resultado_imc)
    
    print(f"\nSeu IMC é: {resultado_imc:.2f}")
    print(f"Classificação: {status}")
