print("Bem vindo ao controle de estoque")

PREÇO=float(input("Por favor insira o preço do produto: "))
ORIGEM=float(input("Por favor, insire o codigo de origem do produto: "))


if ORIGEM==1:
    print("Esse produto tem origem no Sul")

if ORIGEM==2:
    print("Esse produto tem origem no Norte")
    
if ORIGEM==3:
    print("Esse produto tem origem no Leste")
    
if ORIGEM==4:
    print("Esse produto tem origem no Oeste")
    
if ORIGEM==4 or ORIGEM==5:
    print("Esse produto tem origem no Nordeste")

if ORIGEM==7 or ORIGEM==8 or ORIGEM==9:
    print("Esse produto tem origem no Sudeste")

if ORIGEM >= 10 and ORIGEM <=20: 
    print("Esse produto tem origem no Centro-Oeste")

if ORIGEM >= 21 and ORIGEM <=30: 
    print("Esse produto tem origem no Nordeste")

if ORIGEM > 30:
    print("Origem não cadastrada")

