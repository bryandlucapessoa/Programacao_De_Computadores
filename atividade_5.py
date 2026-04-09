nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
resultado1 = nota1 + nota2
resultado2 = resultado1 / 2

if resultado2 >= 7:
    print("APROVADO! sua nota é: {}" .format(resultado2))
elif resultado2 < 5:
    print("REPROVADO sua nota é: {}" .format(resultado2))
elif resultado2 >= 5 and resultado2 < 7:
    print("RECUPERAÇÃO sua nota é: {}" .format(resultado2))