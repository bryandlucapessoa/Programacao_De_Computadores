numb1 = float(input("Digite o valor da sua compra: "))
resultado1 = numb1 / 10 
resultado2 = resultado1 * 9

if numb1 <= 100:
    print("VOCÊ NÃO TEM DESCONTO")
elif numb1 > 100:
    print(f"VOCÊ TEM UM DESCONTO DE 10%! SUA COMPRA FICA {resultado2}")