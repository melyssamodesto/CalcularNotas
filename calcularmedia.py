media = float(input("Digite sua nota:"))

if media >= 7.0:
    print("Aprovado(a).")
else:
    if media >= 4.0:
        print("Necessário realizar prova de recuperação!")
    else:
        print("Reprovado(a).")