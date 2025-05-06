def ler_nota(numero_da_nota):
    while True:
        try:
            nota = float(input(f"Digite a {numero_da_nota}ª nota (de 0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


nota1 = ler_nota(1)
nota2 = ler_nota(2)

media = (nota1 + nota2) / 2

print(f"\nA média do aluno é: {media:.2f}")

if media >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")