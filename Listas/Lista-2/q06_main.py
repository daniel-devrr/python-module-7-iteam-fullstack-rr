import q06_estatisticas as est

notas = []
print("Digite 10 notas:")
while len(notas) < 10:
    try:
        val = float(input(f"Nota {len(notas)+1}: "))
        notas.append(val)
    except ValueError:
        print("Digite um número válido.")

print(f"\nMédia: {est.media(notas)}")
print(f"Mediana: {est.mediana(notas)}")
print(f"Moda: {est.moda(notas)}")
print(f"Desvio Padrão: {est.desvio_padrao(notas)}")