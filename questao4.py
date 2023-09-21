vogais = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'o', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
def oque_eh():
    if caractere in consoantes:
        print("consoante")
    elif caractere in vogais:
        print("vogal")
    elif caractere.isdigit():
        print("número")
    else:
        print("símbolo")

caractere = input()
oque_eh()


