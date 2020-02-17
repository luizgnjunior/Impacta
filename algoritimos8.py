print("Bem vindo Programa peso ideal")

SEXO=str(input("Por favor insira a letra correspondente ao seu sexo.\n Exemplo Mulher = M ou Homem = H"))
ALTURA=float(input("Por favor insira seu Altura"))

if SEXO == "h" or SEXO=="H":
    PESOIDEAL= 72.7*ALTURA-58
    print("Seu peso ideal é de",PESOIDEAL, "Kilos")

if SEXO == "m" or SEXO=="M":
    PESOIDEAL= 62.1*ALTURA-58
    print("Seu peso ideal é de",PESOIDEAL, "Kilos")

if SEXO != "M" and SEXO != "m" and SEXO != "H" and SEXO != "h":

    print("Sexo",SEXO,"Inexistente")
