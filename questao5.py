def media(nota1, nota2, nota3):
    if n3 > 8:
        return (nota1 + nota2 + nota3) / 3 + (1)
    else:
        return (nota1 + nota2 + nota3) / 3


n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))
resultado = media(n1, n2, n3)


def nota_final(nota1, nota2, nota3):
    if resultado > 10.01:
       print("10")
    else:
        print(f'{float(resultado):.2f}')


resultado2 = nota_final(n1, n2, n3)
