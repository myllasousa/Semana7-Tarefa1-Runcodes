def sinal_transito(cor):
    sinal = ["V", "v"]
    if cor in sinal:
        print("Siga")
    elif cor == "A":
        print("Atenção")
    else:
        cor == "E"
        print("Pare")

cor = str(input("")).strip()
sinal_transito(cor)