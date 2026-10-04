print("=== Calculadora de Média Acadêmica ===")

notas = []
contador = 1

while contador <= 3:
    nota = float(input(f"Digite a {contador}ª nota: "))

    while nota < 0 or nota > 10:
        print("Nota inválida. Digite um valor entre 0 e 10.")
        nota = float(input(f"Digite a {contador}ª nota: "))

    notas.append(nota)
    contador += 1

media = sum(notas) / len(notas)

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"\nMédia: {media:.2f}")
print(f"Situação: {situacao}")
