def saudacao(nome, sexo):
    if sexo == 1:
     print(f'Ilmo Sr. {nome}')
    else:
        print(f'Ilma Sra. {nome}')

nome = str(input("")).strip()
sexo = int(input(""))
saudacao(nome, sexo)